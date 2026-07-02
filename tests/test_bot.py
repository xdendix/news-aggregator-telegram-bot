import unittest
from unittest.mock import patch
from types import SimpleNamespace

from bot.handlers import process_message
from bot.services import news_fetcher


class BotBehaviorTests(unittest.TestCase):
    def test_start_saves_user_and_sends_main_menu(self):
        with patch("bot.handlers.save_user") as mock_save_user, patch(
            "bot.handlers.send_message"
        ) as mock_send_message:
            process_message(123, "Ada", "/start")

        mock_save_user.assert_called_once_with(123, "Ada")
        self.assertEqual(mock_send_message.call_count, 1)
        args, kwargs = mock_send_message.call_args
        self.assertIn("Choose a category", args[1])
        self.assertEqual(kwargs["reply_markup"]["inline_keyboard"][0][0]["callback_data"], "menu_national")

    def test_broadcast_requires_admin_and_stops_for_regular_user(self):
        with patch("bot.handlers.send_message") as mock_send_message, patch(
            "bot.handlers.get_all_users"
        ) as mock_get_all_users:
            process_message(999, "Guest", "/broadcast Hello world")

        self.assertIn("not an Admin", mock_send_message.call_args_list[0].args[1])
        mock_get_all_users.assert_not_called()

    def test_portal_callback_uses_supported_rss_key(self):
        with patch("bot.handlers.fetch_news", return_value=[{"title": "A", "link": "#"}]) as mock_fetch_news, patch(
            "bot.handlers.send_message"
        ) as mock_send_message:
            process_message(123, "Ada", "portal_cnn_national")

        mock_fetch_news.assert_called_once_with("cnn_nasional")
        self.assertEqual(mock_send_message.call_count, 2)

    def test_fetch_news_returns_all_entries(self):
        fake_feed = SimpleNamespace(
            bozo=0,
            entries=[
                {"title": "First", "link": "https://a.test", "published": "1"},
                {"title": "Second", "link": "https://b.test", "published": "2"},
            ],
        )

        with patch("bot.services.news_fetcher.feedparser.parse", return_value=fake_feed):
            result = news_fetcher.fetch_news("bbc_world")

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["title"], "First")
        self.assertEqual(result[1]["title"], "Second")


if __name__ == "__main__":
    unittest.main()
