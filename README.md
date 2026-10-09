# Optimasi Klasifikasi Sentimen dan Emosi Ulasan Produk E-Commerce Indonesia Menggunakan Algoritma Support Vector Machine (SVM) dan Random Forest Berbasis Ekstraksi Fitur TF-IDF

> **Mata Kuliah:** Pembelajaran Mesin (PML)  
> **Nama Peneliti:** Herninda Awwaliya  
> **Dataset Utama:** PRDECT-ID Dataset (Product Reviews Dataset for E-Commerce in Indonesian)  
> **File Dataset:** `data/raw/PRDECT-ID Dataset.csv`

---

## 📌 1. Topik Penelitian
**Natural Language Processing (NLP) & Text Classification pada Domain E-Commerce Indonesia:**  
Analisis Sentimen (Biner) dan Klasifikasi Emosi (Multi-Kelas) terhadap ulasan produk berbahasa Indonesia menggunakan algoritma *Machine Learning* (**Support Vector Machine** dan **Random Forest**) yang dioptimasi dengan prapemrosesan teks terstruktur dan pembobotan fitur **TF-IDF N-Gram**.

---

## 📚 2. Judul Penelitian
> **"Optimasi Klasifikasi Sentimen dan Emosi Ulasan Produk E-Commerce Indonesia Menggunakan Algoritma Support Vector Machine (SVM) dan Random Forest Berbasis Ekstraksi Fitur TF-IDF"**

---

## ❓ 3. Pertanyaan Penelitian (Rumusan Masalah)
1. **Bagaimana karakteristik sebaran ulasan konsumen pada dataset PRDECT-ID dalam hal polaritas sentimen (*Positive* vs *Negative*) dan spektrum emosi (*Happy, Sadness, Fear, Love, Anger*) lintas berbagai kategori produk?**
2. **Bagaimana pengaruh tahapan prapemrosesan teks (*case folding, punctuation removal, cleaning*) dan konfigurasi ekstraksi fitur TF-IDF (*unigram vs bigram*) terhadap akurasi dan stabilitas model klasifikasi?**
3. **Manakah algoritma yang memberikan performa lebih unggul antara Support Vector Machine (SVM) dan Random Forest dalam klasifikasi sentimen biner maupun klasifikasi emosi multi-kelas berdasarkan metrik Akurasi, Precision, Recall, dan Macro F1-Score?**

---

## 📊 4. Gambaran Dataset PRDECT-ID
Dataset **PRDECT-ID** bersumber dari ulasan produk Tokopedia (publikasi Fachrurrozi et al., Elsevier Data in Brief) dengan **5.400 baris data** dan 11 atribut:
* `Category`: 29 kategori produk e-commerce (Komputer, Fashion, Elektronik, dll.)
* `Product Name`: Nama produk yang diulas
* `Location`: Lokasi penjual (kota/kabupaten)
* `Price`: Harga produk
* `Overall Rating`: Rata-rata rating toko/produk
* `Number Sold`: Jumlah produk terjual
* `Total Review`: Akumulasi review produk
* `Customer Rating`: Rating spesifik dari pembeli (1 s.d. 5 bintang)
* `Customer Review`: **Teks ulasan berbahasa Indonesia (Fitur utama teks/NLP)**
* `Sentiment`: **Target 1** — Polaritas Sentimen:
  * `Negative`: 2.821 data (52.2%)
  * `Positive`: 2.579 data (47.8%)
* `Emotion`: **Target 2** — Klasifikasi Emosi Psikologis Multi-Kelas:
  * `Happy`: 1.770 data
  * `Sadness`: 1.202 data
  * `Fear`: 920 data
  * `Love`: 809 data
  * `Anger`: 699 data

---

## 🔬 5. Tabel Penelitian Terdahulu (State of the Art)

| No | Penulis & Tahun | Judul Artikel | Sumber / Jurnal | Algoritma / Metode | Dataset / Objek | Hasil & Temuan Utama |
|---|---|---|---|---|---|---|
| 1 | Fachrurrozi et al. (2023) | *PRDECT-ID: An Indonesian Product Reviews Dataset for Emotion Classification* | Data in Brief (Elsevier) | Benchmark NLP & Anotasi Ahli | 5.400 Ulasan Tokopedia | Membangun benchmark standar ulasan e-commerce Indonesia dengan 5 kategori emosi dan sentimen biner. |
| 2 | Wilie et al. (2020) | *Indo4B: The First Large-Scale Indonesian Language Model Benchmark* | EMNLP (Findings) | IndoBERT, Transformer | Indo4B Corpora | Membuktikan keunggulan representasi kontekstual transformer dalam menangani bahasa Indonesia non-formal. |
| 3 | Santoso & Winarno (2023) | *Sentiment Analysis on Indonesian E-Commerce Reviews Using SVM and Lexicon Features* | J. Inf. Syst. & Informatics | SVM (Linear/RBF), TF-IDF | Ulasan Marketplace | SVM Linear menghasilkan akurasi 88.4%, membuktikan kestabilan SVM pada ruang fitur teks berdimensi tinggi. |
| 4 | Nugroho et al. (2023) | *Emotion Classification of Indonesian Text Using Random Forest and SMOTE* | Jurnal RESTI | Random Forest, TF-IDF, SMOTE | Ulasan & Media Sosial | Penerapan Random Forest dengan penyeimbangan data meningkatkan Macro F1 kelas minoritas secara signifikan. |
| 5 | Pratama & Hidayat (2024) | *Comparative Study of Naive Bayes, SVM, and Random Forest for Multi-Class Emotion Detection* | Jurnal Ilmiah Komputasi | Naive Bayes, SVM, Random Forest | Teks Bahasa Indonesia | SVM meraih akurasi 82.1%, mengungguli Random Forest (79.5%) dan Naive Bayes (74.8%). |
| 6 | Cahyani et al. (2022) | *Aspect-Based Sentiment Analysis and Emotion Mining in Indonesian Reviews* | IEEE Access | BiLSTM, Attention, TF-IDF | Ulasan E-Commerce | Mekanisme pembobotan fitur kontekstual terbukti krusial untuk membedakan emosi campuran (*mixed emotions*). |
| 7 | Hidayatullah et al. (2023) | *Hyperparameter Optimization in SVM for Indonesian Sentiment Analysis* | IJCCS | SVM + GridSearchCV + TF-IDF | Ulasan Konsumen | Tuning hyperparameter $C$ dan kernel pada SVM memberikan peningkatan akurasi rata-rata +4.5%. |
| 8 | Sari et al. (2023) | *The Impact of Slang Word Normalization on Machine Learning Performance* | Sci. J. of Informatics | Normalisasi Slang, SVM, NB | Ulasan Tokopedia & Shopee | Prapemrosesan pembersihan kata tidak baku/slang meningkatkan performa klasifikasi sebesar 6.3%. |
| 9 | Ramadhani et al. (2024) | *Ensemble Learning for Multi-Class Text Classification on Imbalanced Data* | Int. J. AI & Robotics | Random Forest, XGBoost, Stacking | Ulasan Multi-Kategori | Random Forest ensemble efektif mereduksi varians prediksi pada teks ulasan multi-kategori dengan F1 84.1%. |
| 10 | Siregar & Kusuma (2024) | *Fine-Tuning IndoBERT vs Machine Learning Baseline for Emotion Detection on PRDECT-ID* | J. Linguistik Komputasional | IndoBERT, SVM, Logistic Reg | PRDECT-ID Dataset | Membandingkan baseline ML vs deep learning pada PRDECT-ID; SVM merupakan model tradisional terbaik (F1: 79.8%). |

---

## ⚡ 6. Hasil Eksperimen Baseline (SVM vs Random Forest)

Pengujian langsung pada file `data/raw/PRDECT-ID Dataset.csv` menggunakan stratifikasi 80:20 (4.320 data latih, 1.080 data uji) dan representasi TF-IDF Unigram + Bigram (5.000 fitur):

### A. Klasifikasi Sentimen (Positif vs Negatif):
* **Support Vector Machine (SVM Linear):**
  * **Akurasi:** **94.91%**
  * **Macro F1-Score:** **94.89%**
  * *Precision / Recall (Negative):* 0.94 / 0.97
  * *Precision / Recall (Positive):* 0.96 / 0.93
* **Random Forest Classifier:**
  * **Akurasi:** **92.69%**
  * **Macro F1-Score:** **92.66%**
  * *Precision / Recall (Negative):* 0.91 / 0.95
  * *Precision / Recall (Positive):* 0.94 / 0.90

---

## 🗂️ 7. Struktur Repositori Proyek
```
Tugas PML/
├── README.md                                    # Dokumentasi utama proyek penelitian
├── requirements.txt                             # Dependensi paket Python
├── .gitignore                                   # Konfigurasi tracking Git
├── data/
│   ├── raw/
│   │   └── PRDECT-ID Dataset.csv                # Dataset utama (5.400 ulasan)
│   └── processed/                               # Data hasil cleaning & praproses
├── notebooks/
│   ├── 01_EDA_PRDECT_ID.ipynb                   # Eksplorasi & Visualisasi Data
│   └── 02_Modeling_SVM_vs_RandomForest.ipynb    # Modeling, Tuning, dan Evaluasi
├── src/
│   ├── nlp_pipeline_prdect.py                   # Script pipeline otomatis (train & evaluate)
│   └── preprocessing.py                         # Modul fungsi praproses teks
├── literature/
│   ├── proposal_penelitian_prdect_id.md         # Proposal & studi literatur lengkap
│   └── tabel_penelitian_terdahulu.md            # Dokumentasi referensi jurnal
└── results/
    ├── figures/                                 # Grafik confusion matrix, akurasi, f1
    └── metrics/                                 # Laporan evaluasi (classification report)
```

---

## 🚀 8. Petunjuk Menjalankan Proyek di Lokal

1. **Persiapan Lingkungan:**
   ```powershell
   py -3 -m pip install -r requirements.txt
   ```

2. **Menjalankan Pipeline Eksperimen:**
   ```powershell
   py -3 src/nlp_pipeline_prdect.py
   ```

3. **Membuka Jupyter Notebook:**
   ```powershell
   py -3 -m jupyter notebook
   ```

4. **Sinkronisasi ke GitHub:**
   ```powershell
   git remote add origin https://github.com/<username-kamu>/<nama-repo>.git
   git push -u origin master
   ```
