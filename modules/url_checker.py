
from urllib.parse import urlparse


def check_url_format(url):

    parsed_url = urlparse(url)

    if parsed_url.scheme not in ["http", "https"]:
        return False, "URL must start with http:// or https://"

    if not parsed_url.hostname:
        return False, "Invalid URL: hostname is missing."

    if " " in url:
        return False, "URL cannot contain spaces."

    return True, "URL format looks valid."
