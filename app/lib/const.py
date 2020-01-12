import re
import nltk
import requests

# for tokenizer
nltk.download("stopwords")
ja_stopword_url = "http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt"
response = requests.get(ja_stopword_url)
ja_stopwords = [w for w in response.content.decode().split("\r\n") if w != ""]
en_stopwords = nltk.corpus.stopwords.words("english")
my_stopwords = [
    "の", ".com", "images", "id", "hatena", "ん", "fotolife", ".jpg", "plain",
    "image", "png", "さ", "at", "%", "n/", "www", "ら", ".s", "()"
]
stopwords = ja_stopwords + en_stopwords + my_stopwords
target_parts_of_speech = ("名詞")
dict_path = "/usr/local/lib/mecab/dic/mecab-ipadic-neologd/"

# 有効なURLかどうか判定する正規表現
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


# error code and msg
invalid_url_code = 2001
invalid_url_msg = "Invalid url"
exception_code = 1000
exception_msg = "Unexpected error"
cannot_scrape_code = 1001
cannot_scrape_msg = "Cannot scrape the article"
cannot_tokenize_code = 1002
cannot_tokenize_msg = "Cannot tokenize the sentence"
cannot_predict_code = 1003
cannot_predict_msg = "Cannot predict the hatebu"

# はてなブログでページが存在していない場合のタイトル
not_exist_title = "Entry is not found"
