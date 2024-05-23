from lib.menu import Menu
from lib.soup import get_soup

url = "https://order.happyorder.io/saigoncity/1579/1232/products/list"


def get_saigon(_):
    food = None
    try:
        soup = get_soup(url)
        food_text = soup.find_all("a")[0].text
        food_items = food_text.split("\n\r")[1:]
        food_items = [item.strip()[4:] for item in food_items]

        food = "\n\n".join(food_items)

    except:
        pass

    return Menu(name="Saigon", url=url, food=food)
