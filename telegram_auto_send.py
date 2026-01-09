import pandas as pd
import requests
from datetime import datetime

# ================== CONFIG ==================
BOT_TOKEN = "8588810986:AAFep03mnWD8NA2n0SLwoscApUi1WchyY0c"
GROUP_ID = "-5227519010"

EXCEL_FILE = r"C:\Users\Asus\Downloads\task_schedular\daily-hindi-words-2026.xlsx"
# ============================================


def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": GROUP_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    requests.post(url, data=payload)


def send_today_messages():
    df = pd.read_excel(EXCEL_FILE)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"]).dt.date

    today = datetime.today().date()

    today_rows = df[df["Date"] == today]

    for _, row in today_rows.iterrows():
        message = (
            "📘 <b>Hindi Word of the Day</b>\n\n"
            f"📝  {row['Massage']}\n"
            f"📖 <b>Meaning:</b> {row['Unnamed: 2']}"
        )
        send_message(message)


# ---------- RUN ----------
send_today_messages()
