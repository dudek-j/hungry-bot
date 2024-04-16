from lib.menu import Menu
from lib.soup import get_soup

url = "https://restaurangjesper.se/veckanslunch/"


def get_jesper(today):
    food = None
    try:
        soup = get_soup(url)
        soup = soup.find_all(p_in_content_node)

        days = [chunk.text for chunk in soup][1:][1::2]
        food = days[today]
    except:
        pass

    return Menu(name="Jesper", url=url, food=food)


def p_in_content_node(tag):
    classes = tag.parent.get("class")
    return classes and "fl-node-content" in classes and tag.name == "p"
