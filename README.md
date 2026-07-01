# Telegram News Aggregator Bot

A modern, real-time Telegram Bot that fetches and aggregates the latest national, technology, and sports news. Built with Python, this project demonstrates industry-standard practices including modular architecture, REST API integration, SQLite database persistence, and an isolated administrative broadcast system.

## Features

- **Real-time Updates:** Utilizes Telegram's Long Polling method to listen and respond to users instantly.
- **Interactive & Dynamic UI/UX:** Replaces basic text commands with modern **Inline Keyboards** for seamless category selection.
- **Dynamic API Routing:** Single-endpoint routing system that dynamically handles news categories (National, Tech, Sports) from external RSS-to-JSON APIs.
- **Database Persistence (SQLite):** Automatically registers and stores unique user demographics securely without server-overhead dependencies.
- **Admin Broadcast System:** Built-in administrative control layer that allows verified admins to send mass announcements to all registered users with block-safety execution.
- **Defensive Programming:** Implemented robust exception handling to ensure continuous uptime during third-party API rate limits.
- **Secure Configuration:** Protects sensitive credentials (`BOT_TOKEN` & `ADMIN_ID`) using environment variables.

## Tech Stack

- **Language:** Python 3.x
- **Database:** SQLite3
- **Libraries:** `requests`, `python-dotenv`
- **API:** Telegram Bot API, RSS2JSON API

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
