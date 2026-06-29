import requests


def get_latest_news():
    # 1. Tembak URL yang aktif
    url = "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fwww.cnnindonesia.com%2Fnasional%2Frss"
    response = requests.get(url)

    # 2. Ubah data mentah dari internet menjadi JSON (dictionary python)
    json_data = response.json()

    # 3. Bongkar JSON
    # Ambil daftar beritanya key-nya bernama 'items'
    news_list = json_data.get("items", [])

    # 4. Siapkan 'kertas kosong' untuk nulis rangkuman berita
    final_text = "BERITA TERBARU HARI INI:\n\n"

    # 5. Bedah isi beritanya dengan looping
    for news in news_list[:4]:
        title = news.get("title")
        link = news.get("link")
        final_text += f"{title}\n🔗 {link}\n\n"

    return final_text
