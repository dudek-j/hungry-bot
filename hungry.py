from datetime import datetime

from lib.slack import send_to_slack
from restaurants.indian_bistro import get_indian_bistro
from restaurants.jesper import get_jesper
from restaurants.kages import get_kages
from restaurants.kebab import get_kebab
from restaurants.lilla_hanoi import get_hanoi
from restaurants.saigon import get_saigon


def main():
    day_of_week = datetime.today().weekday()

    menus = [
        get_hanoi(day_of_week),
        get_kages(day_of_week),
        get_kebab(day_of_week),
        get_jesper(day_of_week),
        get_indian_bistro(day_of_week),
        get_saigon(day_of_week),
    ]

    send_to_slack(menus)


main()
