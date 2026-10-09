"""
evaluation.py — Metrik evaluasi dan visualisasi perbandingan model
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def compute_metrics(y_true, y_pred, model_name: str = "") -> dict:
    """Menghitung MAE, RMSE, dan R² Score."""
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    metrics = {"Model": model_name, "MAE": round(mae, 4), "RMSE": round(rmse, 4), "R2": round(r2, 4)}
    print(f"[{model_name}] MAE={mae:.4f} | RMSE={rmse:.4f} | R²={r2:.4f}")
    return metrics


def compare_models(results: list[dict]) -> pd.DataFrame:
    """Membuat DataFrame perbandingan metrik antar model."""
    df = pd.DataFrame(results)
    df = df.set_index("Model")
    return df


def plot_predictions(y_true, pred_svr, pred_lstm, years, target: str = "Latitude"):
    """Visualisasi prediksi vs nilai aktual."""
    plt.figure(figsize=(10, 5))
    plt.plot(years, y_true, "ko-", label="Aktual", linewidth=2)
    plt.plot(years, pred_svr, "b^--", label="SVR Prediksi", linewidth=1.5)
    plt.plot(years, pred_lstm, "rs--", label="LSTM Prediksi", linewidth=1.5)
    plt.xlabel("Tahun")
    plt.ylabel(f"{target} (°)")
    plt.title(f"Perbandingan Prediksi {target} Kutub Utara Magnetik")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"results/figures/comparison_{target.lower()}.png", dpi=150)
    plt.show()


def plot_metrics_bar(df_metrics: pd.DataFrame):
    """Bar chart perbandingan metrik MAE, RMSE, R²."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    for ax, col in zip(axes, ["MAE", "RMSE", "R2"]):
        df_metrics[col].plot(kind="bar", ax=ax, color=["steelblue", "tomato"])
        ax.set_title(col)
        ax.set_ylabel("Nilai")
        ax.set_xticklabels(df_metrics.index, rotation=0)
        ax.grid(axis="y", alpha=0.3)
    plt.suptitle("Perbandingan Metrik Evaluasi: SVR vs LSTM", fontsize=13, y=1.02)
    plt.tight_layout()
    plt.savefig("results/figures/metrics_comparison.png", dpi=150)
    plt.show()
