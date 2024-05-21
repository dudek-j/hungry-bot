import bs4
import requests


def get_soup(url):
    response = requests.get(url)
    html = response.content.decode("utf-8", "ignore")
    return bs4.BeautifulSoup(html, "html.parser")


def failed_to_get_data():
    return "Failed to parse menu data"
