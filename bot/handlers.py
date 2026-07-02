from .services.database import save_user, get_all_users
from .config import ADMIN_ID
from .telegram_api import send_message
from bot.services.news_fetcher import fetch_news


def process_message(chat_id, sender_name, message_text):

    if not message_text:
        send_message(chat_id, "Please send a valid command.")
        return

    command = message_text.lower()

    if command == "/start" or command == "/news" or command == "menu_main":
        save_user(chat_id, sender_name)
        reply = f"Hello {sender_name}! I am a News Aggregator Bot. Choose a category:"

        keyboard = {
            "inline_keyboard": [
                [{"text": "National News", "callback_data": "menu_national"}],
                [{"text": "International News", "callback_data": "menu_international"}],
            ]
        }
        send_message(chat_id, reply, reply_markup=keyboard)

        # sub-menu national
    elif command == "menu_national":
        reply = "Choose a National News Portal:"
        keyboard = {
            "inline_keyboard": [
                [{"text": "CNN Indonesia", "callback_data": "portal_cnn_national"}],
                [{"text": "Tempo", "callback_data": "portal_tempo_national"}],
                [{"text": "CNBC Indonesia", "callback_data": "portal_cnbc_national"}],
                [{"text": "Back to Main Menu", "callback_data": "menu_main"}],
            ]
        }
        send_message(chat_id, reply, reply_markup=keyboard)

        # sub-menu international
    elif command == "menu_international":
        reply = "Choose a International News Portal:"
        keyboard = {
            "inline_keyboard": [
                [{"text": "BBC World", "callback_data": "portal_bbc_world"}],
                [{"text": "Al Jazeera", "callback_data": "portal_aljazeera"}],
                [{"text": "CNA Asia", "callback_data": "portal_cna_asia"}],
                [{"text": "Back to Main Menu", "callback_data": "menu_main"}],
            ]
        }
        send_message(chat_id, reply, reply_markup=keyboard)

        # Manarik berita
    elif command.startswith("portal_"):
        portal_key = command.replace("portal_", "")
        normalized_key = {
            "cnn_national": "cnn_nasional",
            "tempo_national": "tempo_nasional",
            "cnbc_national": "cnbc_nasional",
            "bbc_world": "bbc_world",
            "aljazeera": "aljazeera",
            "cna_asia": "cna_asia",
        }.get(portal_key, portal_key)
        send_message(chat_id, "Fetching news from portal...")

        # panggil fungsi fetch_news
        data_news = fetch_news(normalized_key)

        if not data_news:
            send_message(
                chat_id, "Failed to retrieve the news. The portal may be down."
            )
            return

        # Rakit datanya di sini
        portal_name = normalized_key.replace("_", " ").upper()
        final_text = f"LATEST NEWS FROM {portal_name}:\n\n"

        for item in data_news[:5]:
            title = item.get("title", "No Title Available")
            link = item.get("link", "#")
            final_text += f"🔹 {title}\n 🔗 {link}\n\n"

        send_message(chat_id, final_text)

    elif command.startswith("/broadcast"):
        if str(chat_id) != str(ADMIN_ID):
            send_message(chat_id, "Sorry, you're not an Admin!")
            return

        broadcast_message = message_text.replace("/broadcast", "", 1).strip()

        # Validasi tambahan: jika admin lupa ketik pesan,
        # jangan kirim pesan kosong
        if not broadcast_message:
            send_message(chat_id, "There are no messages to read")
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
