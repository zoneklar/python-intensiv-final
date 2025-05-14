import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


URLS = [
    "https://google.de",
    "https://gmx.de",
] * 4


def download_page(url):
    return requests.get(url).status_code


def download_pages(urls: list[str]) -> None:
    """Lade Webseiten mit Threads runter."""
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_page, url) for url in urls]

        # auf die Futures warten bis sie fertig sind
        for future in as_completed(futures):
            print("=>", future.result())


def download_pages_map(urls: list[str]) -> None:
    """Lade Webseiten mit Threads runter."""
    with ThreadPoolExecutor() as executor:
        results = executor.map(download_page, urls)
        print(list(results))


download_pages_map(URLS)
