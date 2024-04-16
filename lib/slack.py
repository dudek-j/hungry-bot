import os

import requests


def send_to_slack(menus):
    body = {"blocks": []}

    [append_block(body, menu) for menu in sort_by_name(menus)]
    append_divider(body)

    requests.post(os.environ["HUNGRY_SLACK_URL"], json=body)


def sort_by_name(menus):
    menus.sort(key=lambda menu: menu.name)
    return menus


def append_divider(body):
    body["blocks"].append({"type": "divider"})


def append_block(body, menu):
    append_divider(body)
    body["blocks"].append(menu.message_block())
