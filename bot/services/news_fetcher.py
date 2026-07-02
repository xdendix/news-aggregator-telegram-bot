import feedparser

# RAW RSS links
rss_urls = {
    # National
    "cnn_nasional": "https://www.cnnindonesia.com/nasional/rss",
    "tempo_nasional": "https://nasional.tempo.co/rss",
    "cnbc_nasional": "https://www.cnbcindonesia.com/news/rss",
    # International
    "bbc_world": "https://feeds.bbci.co.uk/news/world/rss.xml",
    "aljazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "cna_asia": "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml",
}


def fetch_news(category_key):
    url = rss_urls.get(category_key)

    if not url:
        return None

    try:
        # ANTI-BLOCKIR: as a Chrome Windows 10
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

        # Eksekusi penarikan data
        feed = feedparser.parse(url, agent=user_agent)

        # Validasi kalai link error atau diblokir
        if feed.bozo == 1 and not feed.entries:
            print(f"Faield fetching RSS from {url}: {feed.bozo_exception}")
            return []

        # Ekstrak data menjadi list
        news_items = []

        # Batasi ambil 5 berita teratas
        for entry in feed.entries[:5]:
            news_items.append(
                {
                    "title": entry.get("title", "No Title Available"),
                    "link": entry.get("link", "#"),
                    "published": entry.get(
                        "published", "No Date"
                    ),  # untuk safety net, kalau portalnya gak ada tanggal
                }
            )

        return news_items

    except Exception as e:
        print(f"Error Sistem Fetcher: {e}")
        return []
