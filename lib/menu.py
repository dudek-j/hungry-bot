from lib.soup import failed_to_get_data


class Menu:
    def __init__(self, name, url, food):
        self.name = name
        self.url = url
        self.food = food

    def message_block(self):
        food = self.food if self.food else failed_to_get_data()

        return {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{self.name}*\n\n {food}",
            },
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Visit website"},
                "url": self.url,
                "action_id": "button-action",
            },
        }
