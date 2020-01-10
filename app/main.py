import nltk
import MeCab
import joblib
import requests
from fastapi import FastAPI

from lib import scraper
from lib import tokenizer
from lib import predictor

app = FastAPI()

# For tokenizer
nltk.download('stopwords')
ja_stopword_url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
response = requests.get(ja_stopword_url)
ja_stopwords = [w for w in response.content.decode().split('\r\n') if w != '']
en_stopwords = nltk.corpus.stopwords.words("english")
my_stopwords =  ["の", ".com", "images", "id", "hatena", "ん", "fotolife", ".jpg", "plain", "image", "png", "さ", "at", "%", "n/", "www", "ら", ".s", "()"]
stopwords = ja_stopwords + en_stopwords + my_stopwords

target_parts_of_speech = ('名詞')

dict_path = "/usr/local/lib/mecab/dic/mecab-ipadic-neologd/"
tagger = MeCab.Tagger(f'-d {dict_path}')

# For model
regressor = joblib.load('/models/regression.pkl')


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/v1/prediction")
def predict(url: str):
    main_text = scraper.scrape(url)
    words = tokenizer.tokenize(main_text, tagger, stopwords, target_parts_of_speech)
    hatebu_num = predictor.predict_hatebu(main_text, words)
    
    return {"はてブ数": hatebu_num}
