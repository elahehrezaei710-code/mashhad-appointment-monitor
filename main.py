import os
import urllib.parse
import urllib.request

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

FORM_URL = "https://ivsf.gsia.gov.af/appointment_form"

message = (
    "یادآوری بررسی نوبت تثبیت هویت ویژه مشهد\n\n"
    "لطفاً فرم را باز کن و پس از واردکردن اطلاعات و تأیید کپچا، "
    "وضعیت ظرفیت را بررسی کن.\n\n"
    "اگر پیام «تاریخ پر است به مشهد» را دیدی، هنوز ظرفیت تکمیل است.\n\n"
    f"لینک فرم: {FORM_URL}\n\n"
    "این ربات فقط یادآوری می‌فرستد و خودش نوبت یا کپچا را بررسی/ثبت نمی‌کند."
)

payload = urllib.parse.urlencode({
    "chat_id": CHAT_ID,
    "text": message,
    "disable_web_page_preview": "true",
}).encode("utf-8")

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
request = urllib.request.Request(url, data=payload, method="POST")

with urllib.request.urlopen(request, timeout=30) as response:
    result = response.read().decode("utf-8")
    if '"ok":true' not in result:
        raise RuntimeError(f"Telegram API returned an unexpected response: {result}")
print("Reminder sent.")
