import requests
import html2text
from readability.readability import Document

from .const import CannotScrapeError, NotHatenaError, not_exist_title, is_hatena_str


def scrape(url: str) -> str:
    try:
        res = requests.get(url)
        if is_hatena_str not in res.content.decode("utf-8"):
            raise NotHatenaError

        article = Document(res.content).summary()
        title = Document(res.content).short_title()

        if title == not_exist_title:
            raise CannotScrapeError

        main_text = html2text.html2text(article)
    except Exception as e:
        raise e

    return main_text
