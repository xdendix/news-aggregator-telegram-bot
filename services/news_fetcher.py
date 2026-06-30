import requests


def get_latest_news(category):
    # Tembak URL yang aktif
    rss_urls = {
        "national": "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fwww.cnnindonesia.com%2Fnasional%2Frss",
        "tech": "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fwww.cnnindonesia.com%2Fteknologi%2Frss",
        "sports": "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fwww.cnnindonesia.com%2Folahraga%2Frss",
    }

    url = rss_urls.get(category)

    try:
        response = requests.get(url, timeout=10)
        json_data = response.json()

        # Debugging: print isi asli dari API
        print("RAW API RESPONSE:", json_data)

        # Cek status dari rss2json
        if json_data.get("status") != "ok":
            return "API Error: API limit exceeded or server is down."

        news_list = json_data.get("items", [])

        # Defensive Programming: cek apakah beritanya beneran ada
        if not news_list:
            return "No news"

        final_text = f"LATEST {category.upper()} NEWS TODAY:\n\n"

        # Bedah isi beritanya dengan looping
        for news in news_list[:4]:
            title = news.get("title")
            link = news.get("link")
            final_text += f"{title}\n🔗 {link}\n\n"

        return final_text

    except Exception as e:
        print(f"Error Fetching News: {e}")
        return "Network Error: Failed to load news."
