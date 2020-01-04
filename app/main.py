import nltk
import joblib
from fastapi import FastAPI

app = FastAPI()
nltk.download('stopwords')
regressor = joblib.load('/models/regression.pkl')


def predict_hatebu(url: str) -> dict:
    pass


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/predict")
def predict(url: str):
    # stopwords test
    stop_words = nltk.corpus.stopwords.words("english")
    return {"stopwords": ",".join(stop_words)}
