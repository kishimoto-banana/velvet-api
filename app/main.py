from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from lib import scraper
from lib import tokenizer
from lib import predictor
from lib.const import (
    url_regex,
    InvalidUrlError,
    NotHatenaError,
    CannotScrapeError,
    CannotTokenizeError,
    CannotPredictError,
    invalid_url_code,
    invalid_url_msg,
    not_hatena_code,
    not_hatena_msg,
    cannot_scrape_code,
    cannot_scrape_msg,
    cannot_tokenize_code,
    cannot_tokenize_msg,
    cannot_predict_code,
    cannot_predict_msg,
    exception_code,
    exception_msg,
)

app = FastAPI()


@app.exception_handler(InvalidUrlError)
def invalid_url_handler(request: Request, exc: InvalidUrlError):
    return JSONResponse(
        status_code=400,
        content={
            "code": invalid_url_code,
            "message": invalid_url_msg,
        },
    )


@app.exception_handler(NotHatenaError)
def not_hatena_handler(request: Request, exc: CannotScrapeError):
    return JSONResponse(
        status_code=500,
        content={
            "code": not_hatena_code,
            "message": not_hatena_msg,
        },
    )


@app.exception_handler(CannotScrapeError)
def cannot_scrape_handler(request: Request, exc: CannotScrapeError):
    return JSONResponse(
        status_code=500,
        content={
            "code": cannot_scrape_code,
            "message": cannot_scrape_msg,
        },
    )


@app.exception_handler(CannotTokenizeError)
def cannot_tokenize_handler(request: Request, exc: CannotTokenizeError):
    return JSONResponse(
        status_code=500,
        content={
            "code": cannot_tokenize_code,
            "message": cannot_tokenize_msg,
        },
    )


@app.exception_handler(CannotPredictError)
def cannot_predict_handler(request: Request, exc: CannotPredictError):
    return JSONResponse(
        status_code=500,
        content={
            "code": cannot_predict_code,
            "message": cannot_predict_msg,
        },
    )


@app.exception_handler(Exception)
def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "code": exception_code,
            "message": exception_msg,
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
    except NotHatenaError:
        raise NotHatenaError
    except CannotScrapeError:
        raise CannotScrapeError
    except CannotTokenizeError:
        raise CannotTokenizeError
    except CannotPredictError:
        raise CannotPredictError
    except Exception:
        raise Exception

    return hatebu_info
