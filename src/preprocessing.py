"""
preprocessing.py — Persiapan dan pembersihan data WMM pole locations
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def load_wmm_data(north_path: str, south_path: str) -> pd.DataFrame:
    """Memuat dataset WMM North & South Pole Locations dan menggabungkannya."""
    col_names = ["longitude", "latitude", "year"]

    north = pd.read_csv(north_path, sep=r"\s+", header=None, names=col_names)
    north["pole"] = "north"

    south = pd.read_csv(south_path, sep=r"\s+", header=None, names=col_names)
    south["pole"] = "south"

    df = pd.concat([north, south], ignore_index=True)
    df["year"] = df["year"].astype(int)
    return df


def load_historical_data(path: str) -> pd.DataFrame:
    """Memuat dataset historis 1590–2025 (format Kaggle/NOAA)."""
    df = pd.read_csv(path)
    df.columns = df.columns.str.lower().str.strip()
    return df


def create_sliding_window(series: np.ndarray, window_size: int = 3):
    """Membuat fitur input X dan target y menggunakan sliding window."""
    X, y = [], []
    for i in range(len(series) - window_size):
        X.append(series[i : i + window_size])
        y.append(series[i + window_size])
    return np.array(X), np.array(y)


def scale_data(train, test):
    """Normalisasi data ke rentang [0, 1] menggunakan MinMaxScaler."""
    scaler = MinMaxScaler()
    train_scaled = scaler.fit_transform(train.reshape(-1, 1))
    test_scaled = scaler.transform(test.reshape(-1, 1))
    return train_scaled.flatten(), test_scaled.flatten(), scaler


if __name__ == "__main__":
    df = load_wmm_data(
        r"data\raw\WMM_North_Pole_Locations_(20202025).csv",
        r"data\raw\WMM_South_Pole_Locations_(20202025).csv",
    )
    print(df)
    df.to_csv(r"data\processed\poles_combined_cleaned.csv", index=False)
    print("Data disimpan ke data/processed/poles_combined_cleaned.csv")
