import re

from lib.menu import Menu
from lib.soup import get_soup

url = "https://www.lillahanoi.com/lunch"


def get_hanoi(today):
    food = None
    try:
        soup = get_soup(url)
        content = soup.find_all(h4_ol_predicate)

        content = [tag.text for tag in content]
        content = [break_weekday(text) for text in content]
        content = flatten(content)
        content = [remove_numbers(text) for text in content]
        content = [text.strip() for text in content if len(text) != 0]
        content = group_by_day(content)

        today = [text.capitalize() for text in content[today]]
        food = "\n".join(today)
    except:
        pass

    return Menu(name="Lilla hanoi", url=url, food=food)


def h4_ol_predicate(tag):
    return tag.name == "h4"


def break_weekday(text):
    return re.split("(måndag|tisdag|onsdag|torsdag|fredag)", text, flags=re.IGNORECASE)


def flatten(xss):
    return [x for xs in xss for x in xs]


def remove_numbers(text):
    return re.sub("[1-9]\\.\\s*", "", text)


def group_by_day(content):
    index = -1
    weekdays = ["måndag", "tisdag", "onsdag", "torsdag", "fredag"]
    result = {}

    for text in content:
        if text.lower() in weekdays:
            index = index + 1
        else:
            result[index] = result.get(index, []) + [text]

    return list(result.values())
