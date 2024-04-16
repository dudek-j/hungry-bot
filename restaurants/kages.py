from lib.menu import Menu
from lib.soup import get_soup

url = "https://kages.se/dagens-lunch/"


def get_kages(today):
    food = None
    try:
        soup = get_soup(url)
        boxes = soup.find_all("div", class_="inner")
        today_box = boxes[today]

        p_with_content = [p.text for p in today_box.find_all(non_empty_p)]
        food = "\n".join(p_with_content[:3])
    except:
        pass

    return Menu(name="Kåges bar", url=url, food=food)


def non_empty_p(tag):
    return (
        len(tag.text.strip()) > 0
        and tag.name == "p"
        and len(tag.find_all("strong")) == 0
    )
