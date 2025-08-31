import requests
from backend.models.query_model import WikiInput
from bs4 import BeautifulSoup
import json

class Scraper:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def scrape(self, topic: WikiInput):
        url = f'https://en.wikipedia.org/wiki/{topic}'
        res = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(res.text, "html.parser")

        main_content = soup.find("div", class_="mw-content-ltr mw-parser-output")
        if not main_content:
            raise ValueError("Could not find main content area")

        elements = main_content.find_all(['h2', 'h3', 'p', 'ul', 'ol', 'dl'])
        results = {}
        current_topic = None

        for element in elements:
            if element.name == 'h2':
                topic_name = element.get_text(strip=True).replace('[edit]', '').strip()
                current_topic = topic_name
                if current_topic not in results:
                    results[current_topic] = []
            elif current_topic and element.name in ['h3', 'p', 'ul', 'ol', 'dl']:
                text = element.get_text(strip=True)
                if text:
                    results[current_topic].append(text)

        return json.dumps(results, indent=4)
