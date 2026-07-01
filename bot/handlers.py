from .services.database import save_user, get_all_users
from .config import ADMIN_ID
from .telegram_api import send_message
from bot.services.news_fetcher import get_latest_news


def process_message(chat_id, sender_name, message_text):

    command = message_text.lower()

    # Routing
    if command == "/start" or command == "/news" or command == "/berita":
        # simpan user di database
        save_user(chat_id, sender_name)
        reply = (
            f"Hello {sender_name}! I am a News Aggregator Bot. Choose a category below:"
        )
        # Rancang bentuk tombolnya (JSON Structure)
        # callback_data sebagai "kode rahasia" yang dikirim ke server saat tombol diklik
        keyboard = {
            "inline_keyboard": [
                [{"text": "National News", "callback_data": "news_national"}],
                [
                    {"text": "Tech News", "callback_data": "news_tech"},
                    {"text": "Sports News", "callback_data": "news_sports"},
                ],
            ]
        }
        send_message(chat_id, reply, reply_markup=keyboard)

    elif command == "/help":
        reply = "Available commands:\n/news - Get the latest news updates!"
        send_message(chat_id, reply)

    elif command.startswith("news_"):
        category = command.split("_")[1]
        send_message(chat_id, f"Fetching {category.capitalize()} News...")
        news_result = get_latest_news(category)
        send_message(chat_id, news_result)

    elif command.startswith("/broadcast"):
        if str(chat_id) != str(ADMIN_ID):
            send_message(chat_id, "Sorry, you're not an Admin!")

        broadcast_message = message_text.replace("/broadcast ", "").strip()

        # Validasi tambahan: jika admin lupa ketik pesan,
        # jangan kirim pesan kosong
        if not broadcast_message:
            send_message(f"There are no messages to read")
            return
        send_message(chat_id, "Send broadcast message to all users")

        # logika pengiriman
        list_users = get_all_users()
        success_count = 0

        for user_id in list_users:
            try:
                send_message(user_id, broadcast_message)
                success_count += 1
            except Exception as e:
                print(f"Faield send to {user_id}: {e}")

        send_message(
            chat_id, f"The broadcast was successfully sent to {success_count} users!"
        )

    else:
        send_message(chat_id, f"Just typing. Your typed: {message_text}")
