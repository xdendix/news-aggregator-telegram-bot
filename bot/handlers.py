from .telegram_api import send_message
from services.news_fetcher import get_latest_news


def process_message(chat_id, sender_name, message_text):

    command = message_text.lower()

    # Routing
    if command == "/start":
        reply = f"Hello {sender_name}! I am a News Aggregator Bot. Type /help to see the menu."
        send_message(chat_id, reply)

    elif command == "/help":
        reply = "Available commands:\n/news - Get the latest news updates!"
        send_message(chat_id, reply)

    elif command == "/news":
        send_message(chat_id, "Fetching the latest news. Please wait...")

        # Panggil fungsi berita
        news_result = get_latest_news()
        send_message(chat_id, news_result)

    else:
        # Echo: Balas dengan membeo
        send_message(chat_id, f"Unrecognize command. Your typed: {message_text}")
