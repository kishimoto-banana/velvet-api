import requests
import html2text
from readability.readability import Document

from .const import CannotScrapeError

# Not foundのとき


def scrape(url: str) -> str:
    try:
        res = requests.get(url)
        article = Document(res.content).summary()
        main_text = html2text.html2text(article)
    except Exception:
        raise CannotScrapeError

    return main_text
