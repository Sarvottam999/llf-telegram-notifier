import requests
import os
from dotenv import load_dotenv

if os.getenv("GITHUB_ACTIONS") != "true":
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
BASE_URL = os.getenv('API_BASE_URL')
API_BASE_URL = BASE_URL + "/api"


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


def login():
    url = f"{API_BASE_URL}/login/"
    payload = {
        "email": EMAIL,
        "password": PASSWORD
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        access_token = response.json()['tokens']['access']
        print("✅ Logged in successfully!")
        return access_token
    except requests.exceptions.RequestException as e:
        error_message = f"❌ Login failed: {e}"
        print(error_message)
        send_telegram_message(error_message)
        return None


def check_pending_inspections(access_token, start_date, end_date):
    url = f"{API_BASE_URL}/dashboard/check-pending/"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    payload = {
        # "start": start_date,
        # "end": end_date
        "days": 1,
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        output = response.json().get('output')
        print("✅ Inspection data fetched!")
        return output
    except requests.exceptions.RequestException as e:
        error_message = f"❌ Failed to fetch inspections: {e}"
        print(error_message)
        send_telegram_message(error_message)
        return None


if __name__ == "__main__":
    access_token = login()
    if access_token:
        output = check_pending_inspections(access_token, "2024-12-01", "2024-12-05")
        if output:
            send_telegram_message(f"🔔 {output}")
