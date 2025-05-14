# import requests

# BOT_TOKEN = '8049462865:AAH-5bsHCHtMfQL_inPHP3V6mOhzcRgqm-4'
# CHAT_ID = '5594600572'

# def send_telegram_message(message):
#     url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
#     payload = {
#         'chat_id': CHAT_ID,
#         'text': message
#     }
#     response = requests.post(url, data=payload)
#     if response.status_code == 200:
#         print("✅ Message sent successfully!")
#     else:
#         print(f"❌ Failed to send message: {response.text}")

# # Test
# send_telegram_message("🔔 Hello! This is a test notification from LLF Notification Bot.")
import requests
import os
from dotenv import load_dotenv

if os.getenv("GITHUB_ACTIONS") != "true":
    load_dotenv()


BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
 

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("✅ Message sent successfully!")
    else:
        print(f"❌ Failed to send message: {response.text}")

send_telegram_message("🔔 Automated message from LLF Bot via GitHub Actions.")
