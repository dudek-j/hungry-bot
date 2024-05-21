from datetime import datetime

from bs4 import Tag

from lib.menu import Menu
from lib.soup import get_soup

url = "https://indianbistro.se/lunch.html"


def get_indian_bistro(today):
    food = None
    try:
        soup = get_soup(url)
        soup = soup.find_all(id="restaurant-menu")[1:]

        if is_week_even():
            food = parse_week(soup[0], today)
        else:
            food = parse_week(soup[1], today)
    except:
        pass

    return Menu(name="Indian bistro", url=url, food=food)


def parse_week(week: Tag, today):
    sections = week.find_all("div", class_="menu-section")
    fixed = [parse_section(section) for section in sections[:3]]
    today = parse_section(sections[3:][today])

    return "\n\n".join(fixed) + "\n\n" + today


def parse_section(today: Tag) -> str:
    items = today.find_all("div", class_="menu-item")
    return "\n\n".join([parse_item(item) for item in items])


def parse_item(item: Tag):
    title = item.find("div", class_="menu-item-name")
    description = item.find("div", class_="menu-item-description")

    if title is None or description is None:
        return ""

    title = title.text.strip()
    description = " ".join(description.text.split())

    return title + ": " + description


def is_week_even():
    return datetime.now().isocalendar()[1] % 2 == 0
