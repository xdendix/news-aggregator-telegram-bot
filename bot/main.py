import requests
import time  # library bawaan python untuk ngatur waktu
from .config import API_TOKEN

from .handlers import process_message


def main():
    print("--- BOT IS RUNNING AND LISTENING FOR MESSAGES (REAL-TIME MODE) ---")
    print("(Press CTRL+C on terminal for turn off bot)")
    update_url = f"https://api.telegram.org/bot{API_TOKEN}/getUpdates"
    last_update_id = None  # biar bot gak baca pesan berulang kali

    while True:
        try:
            # Upgrade ke Long Polling
            # Buat Telegram nahan koneksi selama 30 detik kalau gak ada pesan
            params = {"offset": last_update_id, "timeout": 30}

            # Tambahkan timeout di requests harus lebih besari dari 30
            response = requests.get(update_url, params=params, timeout=35)
            data_bot = response.json()

            if data_bot.get("ok"):
                for item in data_bot.get("result", []):
                    last_update_id = item["update_id"] + 1
                    message = item.get("message", {})

                    if message:
                        # Ekstrak info penting
                        chat_id = message.get("chat", {}).get("id")
                        sender_name = message.get("from", {}).get("first_name", "User")
                        message_text = message.get("text", "")

                        print(f"[{sender_name}]: {message_text}")

                        process_message(chat_id, sender_name, message_text)

        except requests.exceptions.Timeout:
            # Kalau 30 detik tidak ada chat, lanjut putaran
            continue
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(1)  # Jeda jika ada error/internet putus

        # Jeda 1 Detik untuk mengatasi spam agar tidak diblok
        time.sleep(1)


if __name__ == "__main__":
    main()
