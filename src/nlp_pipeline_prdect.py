"""
nlp_pipeline_prdect.py
Pipeline Lengkap: Preprocessing Teks, TF-IDF N-Gram Vectorizer,
Modeling SVM & Random Forest, Evaluasi Metrik, dan Visualisasi Confusion Matrix.
"""
import re
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, f1_score, confusion_matrix


def clean_text_id(text: str) -> str:
    """Membersihkan teks ulasan bahasa Indonesia dari simbol, angka, dan url."""
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_dataset(file_path: str = "data/raw/PRDECT-ID Dataset.csv") -> pd.DataFrame:
    """Memuat dan membersihkan dataset PRDECT-ID."""
    print(f"Memuat dataset dari: {file_path}")
    df = pd.read_csv(file_path)
    df["clean_review"] = df["Customer Review"].apply(clean_text_id)
    return df


def plot_and_save_cm(y_true, y_pred, labels, title: str, filename: str):
    """Menyimpan visualisasi confusion matrix."""
    os.makedirs("results/figures", exist_ok=True)
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    plt.figure(figsize=(7, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
    plt.title(title, fontsize=12, pad=12)
    plt.xlabel("Prediksi", fontsize=10)
    plt.ylabel("Aktual", fontsize=10)
    plt.tight_layout()
    plt.savefig(f"results/figures/{filename}", dpi=150)
    plt.close()
    print(f"Grafik disimpan di: results/figures/{filename}")


def run_experiment(target_col: str = "Sentiment"):
    """
    Menjalankan pengujian klasifikasi teks dengan Support Vector Machine & Random Forest.
    target_col dapat berupa 'Sentiment' (biner) atau 'Emotion' (multi-kelas).
    """
    print(f"\n{'='*60}")
    print(f" MENJALANKAN EKSPERIMEN UNTUK TARGET: {target_col.upper()}")
    print(f"{'='*60}")
    
    df = load_dataset()
    X = df["clean_review"]
    y = df[target_col]
    labels = sorted(y.unique())
    
    # Stratified Split 80:20
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"Data Latih: {len(X_train)} sampel | Data Uji: {len(X_test)} sampel")
    
    # TF-IDF N-Gram (Unigram & Bigram)
    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    # --- MODEL 1: Support Vector Machine (Linear Kernel) ---
    print("\n[1/2] Melatih Support Vector Machine (SVM Linear)...")
    svm = SVC(kernel="linear", C=1.0, random_state=42)
    svm.fit(X_train_vec, y_train)
    y_pred_svm = svm.predict(X_test_vec)
    
    acc_svm = accuracy_score(y_test, y_pred_svm)
    f1_svm = f1_score(y_test, y_pred_svm, average="macro")
    print(f">> [SVM] Akurasi: {acc_svm:.4f} ({acc_svm*100:.2f}%) | Macro F1: {f1_svm:.4f}")
    
    # --- MODEL 2: Random Forest Classifier ---
    print("\n[2/2] Melatih Random Forest (100 Trees)...")
    rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    rf.fit(X_train_vec, y_train)
    y_pred_rf = rf.predict(X_test_vec)
    
    acc_rf = accuracy_score(y_test, y_pred_rf)
    f1_rf = f1_score(y_test, y_pred_rf, average="macro")
    print(f">> [Random Forest] Akurasi: {acc_rf:.4f} ({acc_rf*100:.2f}%) | Macro F1: {f1_rf:.4f}")
    
    # Simpan Confusion Matrix
    plot_and_save_cm(y_test, y_pred_svm, labels, f"Confusion Matrix SVM - {target_col}", f"cm_svm_{target_col.lower()}.png")
    plot_and_save_cm(y_test, y_pred_rf, labels, f"Confusion Matrix Random Forest - {target_col}", f"cm_rf_{target_col.lower()}.png")
    
    # Ringkasan Laporan
    print(f"\n--- Classification Report SVM ({target_col}) ---")
    print(classification_report(y_test, y_pred_svm))
    
    print(f"\n--- Classification Report Random Forest ({target_col}) ---")
    print(classification_report(y_test, y_pred_rf))
    
    return {
        "target": target_col,
        "svm_acc": acc_svm,
        "svm_f1": f1_svm,
        "rf_acc": acc_rf,
        "rf_f1": f1_rf
    }


if __name__ == "__main__":
    # Uji 1: Sentimen (Biner: Positive / Negative)
    res_sent = run_experiment("Sentiment")
    
    # Uji 2: Emosi (Multi-Kelas: Happy, Sadness, Fear, Love, Anger)
    res_emo = run_experiment("Emotion")
    
    print("\n" + "="*60)
    print(" RANGKUMAN HASIL KESELURUHAN EKSPERIMEN")
    print("="*60)
    print(f"Sentimen -> SVM: Akurasi {res_sent['svm_acc']*100:.2f}% | RF: Akurasi {res_sent['rf_acc']*100:.2f}%")
    print(f"Emosi    -> SVM: Akurasi {res_emo['svm_acc']*100:.2f}% | RF: Akurasi {res_emo['rf_acc']*100:.2f}%")
    print("="*60)
