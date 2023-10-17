from typing import List, Tuple, Optional

from .tg_utils import TelegramBot
import io

class MailingLogs:
    def __init__(
            self,
            service_type: str = "Unknown",
            tg_token: Optional[str] = None,
            tg_chat_id: Optional[int] = None
    ):
        self.service_type = service_type

        self.tg_token = tg_token
        self.tg_bot = TelegramBot(self.tg_token) if self.tg_token is not None else None
        self.tg_chat_id = tg_chat_id

        self._logs: List[Tuple[int, int]] = []

    def append(self, chat_id, message_id):
        self._logs.append((chat_id, message_id))

    @property
    def logs(self):
        return self._logs

    def read(self):
        return self._logs

    def logs_to_file(self, filename: str = "logs.csv") -> io.BytesIO:
        out_csv = ""
        for item in self._logs:
            out_csv += f"{item[0]},{item[1]}\n"

        out_csv = out_csv.strip("\n")

        file = io.BytesIO(
            out_csv.encode()
        )
        file.name = filename
        return file

    def send_to_tg(
            self,
            chat_id: Optional[int] = None
    ):
        if self.tg_bot is None:
            raise ValueError("tg_token is None")
        if chat_id is None:
            if self.tg_chat_id is None:
                raise ValueError("chat_id is None")
            chat_id = self.tg_chat_id

        self.tg_bot.send_document(chat_id, self.logs_to_file())
