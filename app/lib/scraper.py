import requests
import html2text
from readability.readability import Document


def scrape(url: str) -> str:
    res = requests.get(url)
    article = Document(res.content).summary()
    main_text = html2text.html2text(article)
    return main_text