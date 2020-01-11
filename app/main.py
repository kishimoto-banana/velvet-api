from fastapi import FastAPI

from lib import scraper
from lib import tokenizer
from lib import predictor

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/v1/prediction")
def predict(url: str):
    main_text = scraper.scrape(url)
    words = tokenizer.tokenize(main_text)
    hatebu_num = predictor.predict_hatebu(main_text, words)

    return {"はてブ数": hatebu_num}
