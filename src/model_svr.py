"""
model_svr.py — Model Support Vector Regression untuk prediksi koordinat kutub
"""
import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import joblib


def build_svr_model(kernel: str = "rbf"):
    """Membuat pipeline SVR dengan MinMaxScaler."""
    pipeline = Pipeline([
        ("scaler", MinMaxScaler()),
        ("svr", SVR(kernel=kernel, C=100, epsilon=0.1, gamma="scale")),
    ])
    return pipeline


def tune_svr(X_train, y_train):
    """Hyperparameter tuning menggunakan GridSearchCV."""
    param_grid = {
        "svr__kernel": ["rbf", "linear"],
        "svr__C": [1, 10, 100],
        "svr__epsilon": [0.01, 0.1, 0.5],
        "svr__gamma": ["scale", "auto"],
    }
    pipeline = Pipeline([("scaler", MinMaxScaler()), ("svr", SVR())])
    grid_search = GridSearchCV(
        pipeline, param_grid, cv=5, scoring="neg_mean_squared_error", n_jobs=-1
    )
    grid_search.fit(X_train, y_train)
    print(f"Best params: {grid_search.best_params_}")
    return grid_search.best_estimator_


def train_svr(X_train, y_train, kernel: str = "rbf"):
    """Melatih model SVR."""
    model = build_svr_model(kernel)
    model.fit(X_train, y_train)
    return model


def save_model(model, path: str):
    joblib.dump(model, path)
    print(f"Model disimpan ke {path}")


def load_model(path: str):
    return joblib.load(path)
