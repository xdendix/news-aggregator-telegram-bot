import sqlite3


def init_db():
    # Python bakal nyari file bot_data.db
    # Kalau belum ada file ini otomatis dibikinin
    conn = sqlite3.connect("bot_data.db")

    # buat cursosr untuk perintah sqlite
    cursor = conn.cursor()

    # Buat table SQL
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            chat_id INTEGER PRIMARY KEY,
            first_name TEXT,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")

    # close semuanya
    conn.commit()  # simpan untuk perubahan
    conn.close()  # tutup filenya, supaya memori gak bocor


print("Database is ready and connected.")


def save_user(chat_id, first_name):
    conn = sqlite3.connect("bot_data.db")
    cursor = conn.cursor()

    try:
        # Insert and ignore: input data baru, tapi kalo chat_id udah ada, biarin aja
        cursor.execute(
            """INSERT OR IGNORE INTO users (chat_id, first_name)
            VALUES (?, ?)""",
            (chat_id, first_name),
        )

        conn.commit()

    except Exception as e:
        print(f"Database Error: {e}")
    finally:
        conn.close()
