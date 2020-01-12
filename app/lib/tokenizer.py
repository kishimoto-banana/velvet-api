import re
import nltk
import MeCab
import requests
import mojimoji

from .const import CannotTokenizeError

nltk.download('stopwords')
ja_stopword_url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
response = requests.get(ja_stopword_url)
ja_stopwords = [w for w in response.content.decode().split('\r\n') if w != '']
en_stopwords = nltk.corpus.stopwords.words("english")
my_stopwords = [
    "の", ".com", "images", "id", "hatena", "ん", "fotolife", ".jpg", "plain",
    "image", "png", "さ", "at", "%", "n/", "www", "ら", ".s", "()"
]
stopwords = ja_stopwords + en_stopwords + my_stopwords

target_parts_of_speech = ('名詞')

dict_path = "/usr/local/lib/mecab/dic/mecab-ipadic-neologd/"
tagger = MeCab.Tagger(f'-d {dict_path}')


def tokenize(sentence: str) -> list:
    sentence = re.sub(r'https?://[\w/:%#\$&\?~\.=\+\-]+', '', sentence)

    tokenized_sentence = []
    regex = re.compile(r'\d')
    regax_one = re.compile(r"^\w$")
    try:
        for chunk in tagger.parse(sentence).splitlines()[:-1]:
            (surface, feature) = chunk.split('\t')
            if feature.startswith(target_parts_of_speech):
                if surface not in stopwords:
                    if not regex.search(surface) and not regax_one.search(
                            surface):
                        word = word_normiraze(surface)
                        tokenized_sentence.append(word)
    except Exception:
        raise CannotTokenizeError

    return tokenized_sentence


def word_normiraze(word: str) -> str:
    word = word.lower()
    word = mojimoji.han_to_zen(word, ascii=False, digit=False)
    word = mojimoji.zen_to_han(word, kana=False)

    return word
