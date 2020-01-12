import math
import joblib
import numpy as np

from .const import CannotPredictError

vectorizer = joblib.load("/models/vectorizer.pkl")
svd = joblib.load("/models/svd.pkl")
classifier = joblib.load("/models/classifier.pkl")
regressor = joblib.load('/models/regression.pkl')


def vectorize(main_text: str, words: list) -> np.array:
    X_bow = vectorizer.transform([" ".join(words)])
    X_svd = svd.transform(X_bow)

    char_nums = len(main_text)
    word_nums = len(words)

    X = np.hstack([
        X_svd,
        np.array(char_nums).reshape(1, -1),
        np.array(word_nums).reshape(1, -1)
    ])
    return X


def predict_is_hatebu(X: np.array) -> bool:
    pred = classifier.predict(X)
    if pred == 1:
        return True
    else:
        return False


def predict_hatebu_num(X: np.array) -> int:
    pred = regressor.predict(X)
    hatebu_num = math.floor(pred + 0.5)
    return hatebu_num


def predict_hatebu(main_text: str, words: list) -> dict:
    try:
        X = vectorize(main_text, words)

        is_hatebu = predict_is_hatebu(X)
        hatebu_num = predict_hatebu_num(X)

        hatebu_info = {"is_hatebu": is_hatebu, "hatebu_num": hatebu_num}
    except Exception:
        raise CannotPredictError

    return hatebu_info
