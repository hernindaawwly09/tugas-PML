"""
nlp_pipeline_prdect.py
Pipeline Preprocessing, Feature Extraction, Training (SVM vs Random Forest),
dan Evaluasi untuk PRDECT-ID Dataset.
"""
import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, f1_score, confusion_matrix


def clean_text_id(text: str) -> str:
    """Membersihkan teks ulasan bahasa Indonesia."""
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)  # Hapus URL
    text = re.sub(r"[^\w\s]", " ", text)                # Hapus tanda baca/simbol
    text = re.sub(r"\d+", " ", text)                    # Hapus angka
    text = re.sub(r"\s+", " ", text).strip()            # Hapus spasi berlebih
    return text


def load_and_preprocess_prdect(file_path: str = "data/raw/PRDECT-ID Dataset.csv") -> pd.DataFrame:
    """Memuat dan membersihkan dataset PRDECT-ID."""
    df = pd.read_csv(file_path)
    df["clean_review"] = df["Customer Review"].apply(clean_text_id)
    return df


def run_experiment(target_col: str = "Sentiment"):
    """
    Menjalankan eksperimen klasifikasi (target_col: 'Sentiment' atau 'Emotion')
    membandingkan SVM dan Random Forest dengan representasi TF-IDF.
    """
    print(f"=== Menjalankan Eksperimen untuk Target: {target_col} ===")
    df = load_and_preprocess_prdect()
    
    X = df["clean_review"]
    y = df[target_col]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Ukuran Data Latih: {len(X_train)} | Data Uji: {len(X_test)}")
    
    # TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    # Model 1: Support Vector Machine (Linear Kernel)
    print("\nTraining Model 1: Support Vector Machine (SVM)...")
    svm_model = SVC(kernel="linear", C=1.0, random_state=42)
    svm_model.fit(X_train_vec, y_train)
    y_pred_svm = svm_model.predict(X_test_vec)
    
    acc_svm = accuracy_score(y_test, y_pred_svm)
    f1_svm = f1_score(y_test, y_pred_svm, average="macro")
    print(f"[SVM] Akurasi: {acc_svm:.4f} | Macro F1-Score: {f1_svm:.4f}")
    
    # Model 2: Random Forest
    print("\nTraining Model 2: Random Forest...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train_vec, y_train)
    y_pred_rf = rf_model.predict(X_test_vec)
    
    acc_rf = accuracy_score(y_test, y_pred_rf)
    f1_rf = f1_score(y_test, y_pred_rf, average="macro")
    print(f"[Random Forest] Akurasi: {acc_rf:.4f} | Macro F1-Score: {f1_rf:.4f}")
    
    print("\n--- Ringkasan Laporan Klasifikasi SVM ---")
    print(classification_report(y_test, y_pred_svm))
    
    print("\n--- Ringkasan Laporan Klasifikasi Random Forest ---")
    print(classification_report(y_test, y_pred_rf))
    
    return {
        "target": target_col,
        "svm_acc": acc_svm,
        "svm_f1": f1_svm,
        "rf_acc": acc_rf,
        "rf_f1": f1_rf
    }


if __name__ == "__main__":
    # Menjalankan untuk Sentimen
    run_experiment(target_col="Sentiment")
