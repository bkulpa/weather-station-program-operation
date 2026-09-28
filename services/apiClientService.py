import os
import urllib.request
import xml.etree.ElementTree as ET
from urllib.error import URLError

STATUS_OK = 200


def get_and_parse_xml_data(path):
    """Retrieve XML data from the IMGW API and return measurement elements."""
    api_url = os.getenv("API_URL")

    if not api_url:
        print("API error: API_URL environment variable is not configured.")
        return []

    try:
        with urllib.request.urlopen(api_url + path, timeout=10) as response:
            if response.getcode() != STATUS_OK:
                raise ValueError(
                    f"API returned HTTP status code {response.getcode()}."
                )

            xml_tree = ET.fromstring(response.read())
            return xml_tree.findall("item")

    except (URLError, ET.ParseError, ValueError) as error:
        print(f"API error: {error}")
        return []
