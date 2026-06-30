from .telegram_api import send_message
from services.news_fetcher import get_latest_news


def process_message(chat_id, sender_name, message_text):

    command = message_text.lower()

    # Routing
    if command == "/start":
        reply = f"Hello {sender_name}! I am a News Aggregator Bot. Choose a menu below:"
        # 1. Rancang bentuk tombolnya (JSON Structure)
        # callback_data sebagai "kode rahasia" yang dikirim ke server saat tombol diklik
        keyboard = {
            "inline_keyboard": [
                [{"text": "National News", "callback_data": "news_national"}]
            ]
        }
        send_message(chat_id, reply, reply_markup=keyboard)

    elif command == "/help":
        reply = "Available commands:\n/news - Get the latest news updates!"
        send_message(chat_id, reply)

    elif command == "/news":
        send_message(chat_id, "Fetching the latest news. Please wait...")

        # Panggil fungsi berita
        news_result = get_latest_news()
        send_message(chat_id, news_result)

    elif command == "news_national":
        send_message(chat_id, "Fetching National News...")
        news_result = get_latest_news()
        send_message(chat_id, news_result)

    else:
        send_message(chat_id, f"Just typing. Your typed: {message_text}")
