from .telegram_api import send_message
from services.news_fetcher import get_latest_news


def process_message(chat_id, sender_name, message_text):

    command = message_text.lower()

    # Routing
    if command == "/start" or command == "/news" or command == "/berita":
        reply = f"Hello {sender_name}! I am a News Aggregator Bot. Choose a category below:"
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

    else:
        send_message(chat_id, f"Just typing. Your typed: {message_text}")
