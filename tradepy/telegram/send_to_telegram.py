import json
import os

import requests

TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")


def send_to_telegram(payload: dict, chat_id=TELEGRAM_CHAT_ID, token=TELEGRAM_TOKEN):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": json.dumps(payload, indent=2),
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }

    requests.post(url, params=params)
