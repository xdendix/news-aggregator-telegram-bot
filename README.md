# Telegram News Aggregator Bot

A modern, real-time Telegram Bot that fetches and aggregates the latest national and international news from RSS feeds. Built with Python, this project demonstrates modular architecture, Telegram API integration, SQLite persistence, and an admin broadcast capability.

## Features

- **Real-time Updates:** Uses Telegram long polling to listen and respond to messages continuously.
- **Menu-driven Navigation:** Supports `/start`, `/news`, and inline keyboard buttons for main menu, national news, and international news.
- **Portal Selection:** Lets users choose from predefined news portals such as CNN Indonesia, Tempo, CNBC Indonesia, BBC World, Al Jazeera, and CNA Asia.
- **RSS News Fetching:** Retrieves headlines from RSS feeds using `feedparser` and formats them into Telegram messages.
- **Database Persistence:** Tracks unique users in a local SQLite database so admin broadcasts can reach registered users.
- **Admin Broadcast System:** Admins can send a `/broadcast <message>` to push announcements to all stored users.
- **Error Handling:** Includes retries and exception handling for network issues and Telegram API timeouts.
- **Environment Configuration:** Uses `.env` variables for `BOT_TOKEN` and `ADMIN_ID`.

## Tech Stack

- **Language:** Python 3.x
- **Database:** SQLite3
- **Libraries:** `requests`, `python-dotenv`, `feedparser`
- **API:** Telegram Bot API
- **Test Framework:** `unittest`

## Preview

![Bot Preview](./assets/bot_preview_1.png)
![Bot Preview](./assets/bot_preview_2.png)
![Bot Preview](./assets/bot_preview_3.png)

## Project Structure

```text
.
├── bot/
│   ├── services/
│   │   ├── database.py       # Handles local database initialization and CRUD operations
│   │   └── news_fetcher.py   # Handles dynamic external API requests & data parsing
│   ├── config.py             # Manages environment variables & security credentials
│   ├── handlers.py           # Core business logic, access control, and message routing
│   ├── main.py               # Long polling engine & main application entry point
│   └── telegram_api.py       # Outbound Telegram messaging services
├── .env.example              # Public configuration template for environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

## How to Run Locally

Follow these steps to run the bot on your local machine:

1. Clone the repository

```bash
git clone [https://github.com/](https://github.com/)[your_github_username]/[your_repo_name].git
cd [your_repo_name]
```

2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/macOS
# .venv\Scripts\activate   # For Windows
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Setup Environment Variables
   Create a new file named .env in the root directory and configure the variables based on .env.example:

```bash
BOT_TOKEN=your_telegram_bot_token_here
ADMIN_ID=your_telegram_chat_id_here
```

5. Run the Bot

```bash
python -m bot.main
```
