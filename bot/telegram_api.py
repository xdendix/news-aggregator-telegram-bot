import requests
from .config import API_TOKEN


# Fungsi untuk balas pesan ke Telegram
def send_message(chat_id, message_text):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    # Payload (data yg dikirim ke server)
    payload = {"chat_id": chat_id, "text": message_text}

    try:
        # Kasih timeout 10 detik untuk safety net kalao koneksi lemot,
        # python gak ngehang selamanya
        response = requests.post(url, json=payload, timeout=10)

        # debug response
        if response.status_code == 200:
            print(f"Reply successfully sent to {chat_id}")
        else:
            print(f"Failed to send message from Telegram: {response.text}")
    except Exception as e:
        print(f"Network error while sending message: {e}")
