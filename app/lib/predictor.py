import math
import joblib
import numpy as np

vectorizer = joblib.load("/models/vectorizer.pkl")
svd = joblib.load("/models/svd.pkl")
regressor = joblib.load('/models/regression.pkl')


def vectorize(main_text: str, words: list) -> np.array:
    X_bow = vectorizer.transform([' '.join(words)])
    X_svd = svd.transform(X_bow)

    char_nums = len(main_text)
    word_nums = len(words)

    X = np.hstack([
        X_svd,
        np.array(char_nums).reshape(1, -1),
        np.array(word_nums).reshape(1, -1)
    ])
    return X


def predict_hatebu(main_text: str, words: list) -> int:
    X = vectorize(main_text, words)
    pred = regressor.predict(X)
    hatebu = math.floor(pred + 0.5)

    return hatebu
