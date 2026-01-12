# MSG-SCHEDULER

A simple message scheduler tool to automate sending messages (e.g., via Telegram).  
This project helps you schedule and automatically send messages at specified times using Python.

## 🧠 Overview

MSG-SCHEDULER is a lightweight Python script that enables you to automate the sending of scheduled messages — ideal for reminders, alerts, or recurring notifications.

## 📁 Project Structure

```

MSG-SCHEDULER/
├── telegram_auto_send.py          # Main Python script to send scheduled messages
├── task-scheduler.bat             # Batch file to run scheduler on Windows
├── import pandas as pd.py         # Script for task/message import (Excel processing)
├── task.xlsx                      # Example data file with schedule info
├── 1_Month_Date_Wise_Messages.xlsx# Example messages & schedule data
├── daily-hindi-words-2026.xlsx    # Example dataset
├── README.md                      # Project documentation
└── …                              # Other supporting files

````

## 🚀 Features

- 📅 Schedule messages for future delivery
- 🤖 Send automated messages (e.g., Telegram)
- 🗂️ Support for Excel-based schedule import
- ⚙️ Runs as Python script or Windows batch process

---

## 🛠️ Prerequisites

Before running MSG-SCHEDULER, make sure you have:

- Python 3.7 or higher
- Telegram Bot Token (if using Telegram API)
- Required Python packages installed

Install dependencies:

```bash
pip install -r requirements.txt
````

*(If you don’t have a `requirements.txt` yet, include packages like `python-telegram-bot`, `pandas`, etc.)*

---

## 📌 How to Use

### 1. Configure the script

Open `telegram_auto_send.py` and:

* Add your Telegram Bot Token
* Specify the user/chat ID(s)
* Set up schedule data (e.g., from an Excel file)

Example inside script:

```python
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
```

### 2. Prepare schedule data

Create an Excel with scheduled times and messages:

| Time             | Message           |
| ---------------- | ----------------- |
| 2026-01-15 09:00 | Happy Birthday!   |
| 2026-01-20 18:30 | Meeting reminder! |

Save it as `task.xlsx`, then update the script to read it.

### 3. Run the scheduler

```bash
python telegram_auto_send.py
```

Or on Windows (if using batch file):

```powershell
./task-scheduler.bat
```

---

## 📝 Example Excel Input

| Scheduled Time   | Message Text         | Recipient |
| ---------------- | -------------------- | --------- |
| 2026-01-15 09:00 | Good morning!        | 123456789 |
| 2026-01-15 12:00 | Lunch time reminder! | 123456789 |

---

## 🧪 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open an issue or submit a PR.

---

## 📄 License

This project is **open source** — feel free to use and modify it!

---

## ❤️ Acknowledgements

Inspired by message scheduler projects and automation scripts on GitHub.

---

