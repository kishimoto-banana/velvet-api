from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from lib import scraper
from lib import tokenizer
from lib import predictor
from lib.const import (
    url_regex,
    InvalidUrlError,
    CannotScrapeError,
    CannotTokenizeError,
    CannotPredictError,
    invalid_url_code,
    cannot_scrape_code,
    cannot_tokenize_code,
    cannot_predict_code,
    exception_code,
)

app = FastAPI()


@app.exception_handler(InvalidUrlError)
def invalid_url_handler(request: Request, exc: InvalidUrlError):
    return JSONResponse(
        status_code=400,
        content={
            "code": invalid_url_code,
            "message": "Invalid URL"
        },
    )


@app.exception_handler(CannotScrapeError)
def cannot_scrape_handler(request: Request, exc: CannotScrapeError):
    return JSONResponse(
        status_code=500,
        content={
            "code": cannot_scrape_code,
            "message": "Cannot scraping"
        },
    )


@app.exception_handler(CannotTokenizeError)
def cannot_tokenize_handler(request: Request, exc: CannotTokenizeError):
    return JSONResponse(
        status_code=500,
        content={
            "code": cannot_tokenize_code,
            "message": "Cannot tokenize"
        },
    )


@app.exception_handler(CannotPredictError)
def cannot_predict_handler(request: Request, exc: CannotPredictError):
    return JSONResponse(
        status_code=500,
        content={
            "code": cannot_predict_code,
            "message": "Cannot predict"
        },
    )


@app.exception_handler(Exception)
def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "code": exception_code,
            "message": "Unexpected error"
        },
    )


@app.get("/v1/prediction")
def predict(url: str):
    if not url_regex.search(url):
        raise InvalidUrlError

    try:
        main_text = scraper.scrape(url)
        words = tokenizer.tokenize(main_text)
        hatebu_info = predictor.predict_hatebu(main_text, words)
    except CannotScrapeError:
        raise CannotScrapeError
    except CannotTokenizeError:
        raise CannotTokenizeError
    except CannotPredictError:
        raise CannotPredictError
    except Exception:
        raise Exception

    return hatebu_info
