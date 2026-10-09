# Prediksi Pergeseran Lokasi Kutub Utara Magnetik Bumi Menggunakan LSTM dan SVR

> **Mata Kuliah:** Pembelajaran Mesin (PML)  
> **Nama:** Herninda Awwaliya  
> **Dataset Utama:** WMM North & South Pole Locations (2020–2025) — NOAA/BGS  
> **Dataset Tambahan:** Wandering of the Geomagnetic Poles (1590–2025) — NOAA/Kaggle

---

## 📌 Topik Penelitian
Prediksi posisi **Kutub Utara Magnetik Bumi** berdasarkan koordinat historis (longitude dan latitude) menggunakan pendekatan *machine learning* dan *deep learning*.

## 📚 Judul Penelitian
**"Optimasi Prediksi Lokasi Kutub Utara Magnetik Bumi Menggunakan Algoritma LSTM dan SVR Berbasis Data World Magnetic Model (WMM) NOAA"**

---

## ❓ Pertanyaan Penelitian
1. Bagaimana pola pergeseran lokasi Kutub Utara Magnetik Bumi berdasarkan data WMM NOAA tahun 1590–2025?
2. Apakah algoritma LSTM lebih unggul dibandingkan SVR dalam memprediksi koordinat (longitude, latitude) pergeseran Kutub Utara Magnetik Bumi?
3. Metrik evaluasi apa (MAE, RMSE, R²) yang paling signifikan membedakan performa kedua algoritma tersebut?

---

## 🗂️ Struktur Proyek
```
Tugas PML/
├── README.md
├── data/
│   ├── raw/
│   │   ├── WMM_North_Pole_Locations_(20202025).csv
│   │   ├── WMM_South_Pole_Locations_(20202025).csv
│   │   └── geomagnetic_poles_1590_2025.csv      ← dataset tambahan (Kaggle/NOAA)
│   └── processed/
│       └── poles_combined_cleaned.csv
├── notebooks/
│   ├── 01_EDA.ipynb                              ← Exploratory Data Analysis
│   ├── 02_Preprocessing.ipynb
│   ├── 03_Model_SVR.ipynb
│   ├── 04_Model_LSTM.ipynb
│   └── 05_Evaluation_Comparison.ipynb
├── src/
│   ├── preprocessing.py
│   ├── model_svr.py
│   ├── model_lstm.py
│   └── evaluation.py
├── results/
│   ├── figures/
│   └── metrics/
├── literature/
│   └── tabel_penelitian_terdahulu.md
└── requirements.txt
```

---

## 🔧 Cara Menjalankan

```bash
# 1. Clone repo
git clone https://github.com/<username>/tugas-pml.git
cd tugas-pml

# 2. Install dependencies
pip install -r requirements.txt

# 3. Jalankan notebook urut dari 01 → 05
jupyter notebook notebooks/
```

---

## 📊 Dataset
| Dataset | Sumber | Tahun | Keterangan |
|---------|--------|-------|------------|
| WMM North Pole Locations | NOAA/BGS | 2020–2025 | Longitude, Latitude, Year |
| WMM South Pole Locations | NOAA/BGS | 2020–2025 | Longitude, Latitude, Year |
| Geomagnetic Poles 1590–2025 | NOAA/Kaggle | 1590–2025 | Dataset historikal lengkap |

---

## 🤖 Algoritma
- **LSTM** (Long Short-Term Memory) — Deep Learning untuk data sekuensial
- **SVR** (Support Vector Regression) — ML berbasis kernel untuk regresi non-linear

## 📈 Metrik Evaluasi
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## 📝 Lisensi
Dataset WMM bersumber dari NOAA/BGS (domain publik). Dataset historis geomagnetic dari Kaggle.
