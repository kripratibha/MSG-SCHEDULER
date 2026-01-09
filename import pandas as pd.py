import pandas as pd
import requests
from datetime import datetime

BOT_TOKEN = "8588810986:AAFep03mnWD8NA2n0SLwoscApUi1WchyY0c"
CHAT_ID = "1381196377"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=payload)

def send_today_messages():
    df = pd.read_excel("messages.xlsx")
    today = datetime.today().strftime("%Y-%m-%d")

    today_msgs = df[df['date'] == today]

    for msg in today_msgs['message']:
        send_message(msg)

send_today_messages()
