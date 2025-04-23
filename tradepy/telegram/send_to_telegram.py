import os

import requests

TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")


def send_to_telegram_text(
    text: str,
    chat_id=TELEGRAM_CHAT_ID,
    token=TELEGRAM_TOKEN,
) -> None:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": text,
    }

    response = requests.post(url, params=params)
    response.raise_for_status()


def send_to_telegram(
    text: str,
    chat_id=TELEGRAM_CHAT_ID,
    token=TELEGRAM_TOKEN,
) -> None:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }

    response = requests.post(url, params=params)
    response.raise_for_status()
