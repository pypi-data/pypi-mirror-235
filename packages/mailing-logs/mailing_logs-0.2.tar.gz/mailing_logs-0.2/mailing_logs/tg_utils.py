import io

import requests


class TelegramBot:
    def __init__(
            self,
            tg_token: str,
            api_url: str = "https://api.telegram.org/bot"
    ):
        self.tg_token = tg_token
        self.api_url = api_url

        self.api_endpoint = self.api_url + self.tg_token

    def send_document(self, chat_id: int, document: io.BytesIO):
        url = f'{self.api_endpoint}/sendDocument?chat_id={chat_id}'
        return requests.get(
            url,
            files={'document': document}
        ).json()
