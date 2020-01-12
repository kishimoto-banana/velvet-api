import re

url_regex = re.compile(r"https?://[\w/:%#\$&\?~\.=\+\-]+")


# exception class
class InvalidUrlError(Exception):
    """有効なURLでは無かったときに投げるエラー"""


class CannotScrapeError(Exception):
    """スクレイピングに失敗したときに投げるエラー"""


class CannotTokenizeError(Exception):
    """分かち書きに失敗したときに投げるエラー"""


class CannotPredictError(Exception):
    """はてブの予測に失敗したときに投げるエラー"""


# error code
invalid_url_code = 2001
exception_code = 1000
cannot_scrape_code = 1001
cannot_tokenize_code = 1002
cannot_predict_code = 1003

not_exist_title = "Entry is not found"
