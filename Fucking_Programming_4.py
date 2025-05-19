# Connect to the Telegram account by Access Token on 1403/09/04
# 
# Verbinden Sie sich mit dem Telegram-Konto per Access Token am 1403/09/04

import os, requests
# from telegram import Bot

if (os.name == "nt"):
    _ = os.system("cls")

TELEGRAM_TOKEN = "7824110175:AAGmttzZDz60DcFGCaWdsieCs3ymeUhhtLY"
GET_UPDATES_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
SEND_MESSAGE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

CHAT_ID = 670023094
MESSAGE = "سلام! این پیام آزمایشی است."
payload = {
    "chat_id": CHAT_ID,
    "text": MESSAGE
}
last_update_id = None  # مقدار اولیه برای آخرین update_id

while True:  # یک حلقه برای اجرای مداوم کد
    try:
        # دریافت به‌روزرسانی‌ها با استفاده از offset
        # دریافت پیام‌های جدید
        params = {"offset": last_update_id + 1} if last_update_id else {}
        response = requests.get(GET_UPDATES_URL, params=params)
        updates = response.json()

        if updates["ok"] and updates["result"]:
            for update in updates["result"]:
                # استخراج اطلاعات پیام
                update_id = update["update_id"]
                chat_id = update["message"]["chat"]["id"]
                message_text = update["message"].get("text", "")

                # پاسخ به پیام‌ها
                if message_text == "/start":
                    response_text = "سلام! به ربات من خوش آمدید. 😊"
                elif message_text == "/help":
                    response_text = "دستورات موجود:\n/start - شروع\n/help - راهنما"
                else:
                    response_text = "دستور شما نامعتبر است. لطفاً دوباره تلاش کنید."

                # ارسال پاسخ
                payload = {"chat_id": chat_id, "text": response_text}
                requests.post(SEND_MESSAGE_URL, json=payload)

                # به‌روزرسانی آخرین update_id
                last_update_id = update_id

    except Exception as e:
        print(f"Error: {e}")
        break
