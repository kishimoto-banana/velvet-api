import requests
import html2text
from readability.readability import Document

from .const import CannotScrapeError, not_exist_title


def scrape(url: str) -> str:
    try:
        res = requests.get(url)
        article = Document(res.content).summary()
        title = Document(res.content).short_title()

        if title == not_exist_title:
            raise CannotScrapeError

        main_text = html2text.html2text(article)
    except Exception:
        raise CannotScrapeError

    return main_text
