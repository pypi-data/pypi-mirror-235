# -*- coding: utf-8 -*-
import re
from ipaddress import ip_address, ip_network
import csv
import iocextract
import urllib.parse
from .ioc_types import *

# Text that might wrap an IOC, in format <start txt>, <end txt>
# So for example "(10.20.32.123)" -> "10.20.32.123"
WRAPPING_CHARS = [
    ("(", ")"),
    ("<", ">"),
    (";", ";"),
    ("[", "]"),
    ("-", "-"),
    ('"', '"'),
    ("'", "'"),
    (";", ";"),
    ("href=\"", "\""),
    ("alt=\"", "\""),
]
SPLIT_EXPRESSIONS = []
for pair in WRAPPING_CHARS:
    re_str = r"{start}(.+?){end}".format(start=re.escape(pair[0]), end=re.escape(pair[1]))
    SPLIT_EXPRESSIONS.append(re.compile(re_str))

COMMON_DELIMITERS = [
    ",",
    ";",
    "[<>]",
]

extract_domain_or_ip = re.compile("^https?(?:://)?(.+?)(/|$|\?)")

# Order of this list determines the detection order, DO NOT CHANGE
# Generally, add new types to the top of this list
IOC_TYPES_SEARCH_ORDER = [
    'ssdeep',
    'sha256',
    'sha1',
    'md5',
    'email',
    'ipv4_public',
    'ipv4_private',
    'ipv6_public',
    'ipv6_private',
    'domain',
    'filename',
    'url',
    'unknown'
]

DEFANGABLE = ['domain', 'ipv4_private', 'ipv4_public', 'url']

IOC_PATTERNS = {
    'ipv4_public': IPv4PublicIOC(),
    'ipv4_private': IPv4PrivateIOC(),
    'ipv6_public': IPv6PublicIOC(),
    'ipv6_private': IPv6PrivateIOC(),

    'url': URLIOC(),
    'email': RegexIOC(r'^[\w%+.-]+@[A-Za-z0-9.-]+\.[a-z]{2,}$'),
    'md5': RegexIOC(r'^[a-fA-F0-9]{32}$'),
    'sha1': RegexIOC(r'^[a-fA-F0-9]{40}$'),
    'sha256': RegexIOC(r'^[a-fA-F0-9]{64}$'),
    'ssdeep': RegexIOC(r'^([1-9]\d*)(?!:\d\d($|:)):([\w+0-9\/]+):([\w+0-9\/]+)$'),
    'filename': FilenameIOC(),
    'domain': DomainIOC(),
    'unknown': AnyIOC()
}


def _unravel(value):
    """
    Pull out any strings that are wrapped by common separators (WRAPPIN_CHARS)
    :param value: The text to pull substrings out of.
    :return: A list of substrings that were found.
    """
    to_return = []
    for expression in SPLIT_EXPRESSIONS:
        match = expression.findall(value)
        if match:
            to_return.extend(match)
    return to_return


def _split_on_possible_separators(value):
    """
    Split the input string on common characters used as delimiters
    :param value: The text to split
    :return: a list of substrings after splitting
    """
    to_return = []
    for delimiter in COMMON_DELIMITERS:
        to_return.extend(re.split(delimiter, value))
    return to_return




def _possible_entries(entry):
    """
    Pull out any substrings that are likely a single unit based on common syntax patterns.
    :param entry: The text to pull substrings out of.
    :return: A list of substrings that were found.
    """

    poss = []
    poss.extend(_unravel(entry))
    poss.extend(_split_on_possible_separators(entry))
    poss.append(entry)

    return poss


def _defang_results(results):
    """
    Defang any IOC types that we can (see DEFANGABLE)
    :param results: A dictionary with the ioc type as the key and a list of iocs for each value.
    :return: The same as the results input, but any values that could be defanged are.
    """
    new_results = {}
    for key, value in results.items():
        if key in DEFANGABLE:
            new_value = []
            for ioc in value:
                new_value.append(iocextract.defang(ioc))
            new_results[key] = new_value
    results.update(new_results)
    return results


def generate_domain_regex(whitelist_domains):
    all_regex = []
    for domain in whitelist_domains:
        domain = domain.strip()
        escaped_domain = re.escape(domain)
        domain_re = re.compile(rf'^([\w-]+\.)*{escaped_domain}$', re.I)
        all_regex.append({'ioc_type': 'domain', 'expression': domain_re})
        url_re = re.compile(rf'^https?:\/\/([\w-]+\.)*{escaped_domain}(\/.*)?', re.I)
        all_regex.append({'ioc_type': 'url', 'expression': url_re})
    return all_regex


def type_iocs(iocs, iocs_to_parse):
    result = {}
    for key in iocs_to_parse:
        result[key] = []
    for ioc in iocs:
        typ = type_ioc(ioc, iocs_to_parse)
        if typ != "unknown":
            result[typ].append(ioc)
        for test in _possible_entries(ioc):
            typ = type_ioc(test, iocs_to_parse)
            if typ != "unknown":
                result[typ].append(test)
            else:
                # iocextract will find defanged iocs, so we have to try refanging to type those.
                defanged = iocextract.defang(test)
                defang_type = type_ioc(defanged, iocs_to_parse)
                if defang_type != "unknown":
                    result[defang_type].append(defanged)
    return result


def remove_whitelisted_ips(result, ip_cidrs):
    for ip_type in ['ipv4_public', 'ipv4_private', 'ipv6_public', 'ipv6_private']:
        remove = []
        for ip in result.get(ip_type, []):
            for ip_range in ip_cidrs:
                if ip_address(ip) in ip_range:
                    remove.append(ip)
        for ip in remove:
            result[ip_type].remove(ip)
    return result


def remove_ip_whitelisted_urls(urls, ip_cidrs):
    remove = set()
    for url in urls:
        domain_or_ip = re.search(extract_domain_or_ip, urllib.parse.unquote(url)).group(1)
        try:
            for ip_range in ip_cidrs:
                if ip_address(domain_or_ip) in ip_range:
                    remove.add(url)
        except ValueError:
            pass
    for url in remove:
        urls.remove(url)
    return urls


def remove_whitelisted_iocs(result, whitelists, iocs_to_parse):
    for expression in whitelists:
        if expression['expression']:
            if expression['ioc_type'] == 'all':
                for ioc_typ in iocs_to_parse:
                    ioc_list = []
                    for ioc in result[ioc_typ]:
                        if re.findall(expression['expression'], ioc):
                            pass  # Found match, don't add to list
                        else:
                            ioc_list.append(ioc)
                    result[ioc_typ] = ioc_list
            else:
                ioc_list = []
                for ioc in result[expression['ioc_type']]:
                    if re.findall(expression['expression'], ioc):
                        pass  # Found match, don't add to list
                    else:
                        ioc_list.append(ioc)
                result[expression['ioc_type']] = ioc_list
    return result


def parse_iocs(text, defang=False, whitelist_regex='', iocs_to_parse=None,
               whitelist_domains=None, whitelist_ip_cidr_ranges=None, use_ml_model=False):
    """
    Extract all IOCs from the given text.
    :param text: A string to parse.
    :param defang: If True, defang any IOCs we can (see DEFANGABLE). If False, return IOCs in their fanged state.
    :param whitelist_regex: Any IOC matching this regex will be ignored
    :param iocs_to_parse: A list of IOC types to look for (see IOC_TYPES_SEARCH_ORDER for options)
    :param whitelist_domains: A list or CSV of domains to exclude from results.  Excludes domains and URLs that match
    :param whitelist_ip_cidr_ranges: A list or CSV of CIDR ranges to exclude from results.
    :param use_ml_model: BETA feature to use an ML model to identify iocs.
    Excludes IPs and URLs that match
    :return: A dictionary with the ioc type as the key and a list of iocs for each value.
    """
    if iocs_to_parse is not None:
        if len(iocs_to_parse) == 1 and iocs_to_parse[0] == 'all':
            iocs_to_parse = IOC_TYPES_SEARCH_ORDER
        for ioc in iocs_to_parse:
            if ioc not in IOC_TYPES_SEARCH_ORDER:
                raise ValueError(f"{ioc} is not a valid IOC type. Valid IOCs are: {', '.join(IOC_TYPES_SEARCH_ORDER)}")
    else:
        iocs_to_parse = IOC_TYPES_SEARCH_ORDER

    all_whitelist_regex = [{'ioc_type': 'all', 'expression': whitelist_regex}]
    if whitelist_domains is None:
        whitelist_domains = []
    elif isinstance(whitelist_domains, str):
        whitelist_domains = list(csv.reader([whitelist_domains]))[0]
    all_whitelist_regex.extend(generate_domain_regex(whitelist_domains))

    if whitelist_ip_cidr_ranges is None:
        whitelist_ip_cidr_ranges = []
    elif whitelist_ip_cidr_ranges and isinstance(whitelist_ip_cidr_ranges, str):
        whitelist_ip_cidr_ranges = list(csv.reader([whitelist_ip_cidr_ranges]))[0]
    whitelist_ip_cidr_ranges = [ip_network(cidr) for cidr in whitelist_ip_cidr_ranges]

    text2 = urllib.parse.unquote(text)
    text_chunks = set()
    text_versions = [text, text2]
    for text_input in text_versions:
        split_text = re.split(r"(\n| )", text_input)
        split_text = map(lambda x: x.strip("\r\t\n "), split_text)
        split_text = filter(lambda x: len(x) > 2, split_text)  # Strip out single chars
        text_chunks.update(split_text)

    if use_ml_model:
        # Takes a while to import this and it isn't adding much value yet, so I only import it if it is requested to
        #  be used.
        import spacy

        dir = os.path.dirname(os.path.abspath(__file__))
        model_location = os.path.join(dir, "models", "ioc_model")
        model = spacy.load(model_location)

        doc = model(text)
        for ent in doc.ents:
            text_chunks.add(ent.text)

    # iocextract can find iocs that have been defanged.  They are refanged and added to the correct type.
    # Patched: iocextract has bug in yara regex for long strings causing exponential back string matches.
    # This chain call is the same as extract_iocs except yara is removed.  We tried doing a timeout on
    # the call that searched for yara, but the timeout wrapper wasn't windows compatible.
    if "url" in iocs_to_parse:

        found = list(iocextract.extract_urls(text, refang=False, strip=False))
        text_chunks.update(found)
        text_chunks.update([iocextract.refang_url(x) for x in found])
    if {"ipv4_public", "ipv4_private", "ipv6_public", "ipv6_private"}.intersection(iocs_to_parse):
        found = list(iocextract.extract_ips(text, refang=False))
        text_chunks.update(found)
        text_chunks.update([iocextract.refang_ipv4(x) for x in found])
    if "email" in iocs_to_parse:
        found = list(iocextract.extract_emails(text, refang=False))
        text_chunks.update(found)
        text_chunks.update([iocextract.refang_email(x) for x in found])
    if {'sha512', 'sha256', 'sha1', 'md5'}.intersection(set(iocs_to_parse)):
        text_chunks.update(iocextract.extract_hashes(text))

    result = type_iocs(text_chunks, iocs_to_parse)
    # remove duplicates
    for k, v in result.items():
        result[k] = list(set(v))

    if {'domain', 'ipv4_public', 'ipv4_private', 'ipv6_public', 'ipv6_private'}.intersection(iocs_to_parse):
        # Append domains and ips from URLs to the domains/ips result
        cleaned_urls = [re.search(extract_domain_or_ip, urllib.parse.unquote(u)).group(1) for u in
                        result.get("url", [])]  # Strip schema
        domains_and_iocs = type_iocs(cleaned_urls, iocs_to_parse)
        for ioc_type, ioc in result.items():
            ioc.extend(domains_and_iocs.get(ioc_type, []))
        if 'domain' in iocs_to_parse:
            for ioc in cleaned_urls:
                if DomainIOC().run(ioc, check_tld=False):
                    result['domain'].append(ioc)

        # remove duplicates
        for k, v in result.items():
            result[k] = list(set(v))

    # Clear results based on whitelist
    result = remove_whitelisted_iocs(result, all_whitelist_regex, iocs_to_parse)

    # Clear results based on IP whitelist
    result = remove_whitelisted_ips(result, whitelist_ip_cidr_ranges)

    # Clear URLs base on IP whitelist
    if 'url' in result:
        result['url'] = remove_ip_whitelisted_urls(result['url'], whitelist_ip_cidr_ranges)

    if 'domain' in result:
        stripped_domains = set()
        for domain in result['domain']:
            if domain.startswith("www."):
                stripped_domains.add(domain[4:])
            else:
                stripped_domains.add(domain)
        result['domain'] = list(stripped_domains)

    if defang:
        result = _defang_results(result)

    return result


def is_ip(value):
    """
    Determine whether the given value is an IP address.
    :param value: A string.
    :return: True if value is an IP address, False if not.
    """
    versions = ["4", "6"]
    p_levels = ["public", "private"]
    for v in versions:
        for p_level in p_levels:
            if IOC_PATTERNS["ipv{}_{}".format(v, p_level)].run(value):
                return True
    return False


def type_ioc(ioc, types_to_find=None):
    """
    Determine what type of IOC a string is.
    :param ioc: The IOC to classify.
    :param types_to_find: A list of types you want to look for.
    :return: The type of the IOC as a string, (see IOC_TYPES_SEARCH_ORDER for options)
    """
    iocs = types_to_find if types_to_find is not None else IOC_TYPES_SEARCH_ORDER
    for pat_name in IOC_TYPES_SEARCH_ORDER:
        # The order that the types are checked in matters, so we need to iterate over IOC_TYPES
        if pat_name in iocs:
            if IOC_PATTERNS[pat_name].run(ioc):
                return pat_name
    return "unknown"
