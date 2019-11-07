import io
import zipfile
import requests

from bs4 import BeautifulSoup

from .constant import DATA_URL


def get_subset_links() -> list:
    """
    Get list of links for subsets of data.

    Returns:
        list: list of URLs to the zipped subsets
    """

    site = requests.get(DATA_URL)
    soup = BeautifulSoup(site.content, features="html.parser")

    links = []

    for link in soup.find_all("a"):
        if "zip" in link.get("href"):
            links.append(link.get("href"))

    return links


def download_zip(zip_url: str) -> (str, str):
    """
    Args:
        zip_url (str): URL to a zip subset of the data

    Returns:
        (str, str): file_name and content of the file that is included in the zip archiv

    Raises:
        HTTPError: Will be raised if the ``zip_url`` responsed a not 200 code
    """

    try:
        request = requests.get(zip_url)

    except Exception:
        raise requests.HTTPError(f"Could not get URL: {zip_url}")


    if request.status_code == 200:
        zip_file_bytes = io.BytesIO(request.content)
        zipped_sub_set = zipfile.ZipFile(zip_file_bytes)

        # Zip archives only contain a single file
        file_name = zipped_sub_set.namelist()[0]

        return file_name, zipped_sub_set.read(file_name).decode("utf8")

    else:
        raise requests.HTTPError(f"Could not get URL: {zip_url}")
