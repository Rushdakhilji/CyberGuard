
import requests
import ipaddress


def lookup_ip(ip_address):

    # Validate the IP address
    try:
        ipaddress.ip_address(ip_address)
    except ValueError:
        return None

    url = f"https://ipwho.is/{ip_address}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if not data.get("success"):
            return None

        connection = data.get("connection", {})

        return {
            "ip": data.get("ip", "N/A"),
            "city": data.get("city", "N/A"),
            "region": data.get("region", "N/A"),
            "country": data.get("country", "N/A"),
            "organization": connection.get("org", "N/A"),
            "isp": connection.get("isp", "N/A")
        }

    except (requests.exceptions.RequestException, ValueError):
        return None
