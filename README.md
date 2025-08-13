# Data-Cleaning-Transformation

# 🏙️ Airbnb Listings Analysis

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

A data analysis project exploring Airbnb listings to uncover pricing trends, availability patterns, and neighbourhood insights.  
Using **Python**, **Pandas**, **Matplotlib**, and **Seaborn** for data manipulation and visualization.

---

## 📌 Project Overview
The goal of this project is to:
- Clean and preprocess raw Airbnb listings data.
- Perform **exploratory data analysis (EDA)**.
- Identify patterns in prices, availability, and location-based trends.
- Store cleaned datasets in a SQL database for further analysis.

---

## 📊 Sample Visualizations
| Missing Values Heatmap | Price Distribution |
|------------------------|--------------------|
| ![Missing Values Heatmap](assets/missing_values_heatmap.png) | ![Price Distribution](assets/price_distribution.png) |

| Listings by Neighbourhood Group | Correlation Heatmap |
|--------------------------------|---------------------|
| ![Neighbourhood Group Count](assets/listings_by_group.png) | ![Correlation Heatmap](assets/correlation_heatmap.png) |

---

## 📂 Project Structure
```plaintext
data-cleaning-transformation/
│
├── data/
│   ├── raw/        # Raw datasets
│   └── cleaned/    # Processed datasets
│
├── notebooks/      # Jupyter notebooks for EDA & cleaning
│   ├── cleaning.ipynb
│   └── analysis.ipynb
│
├── scripts/        # Python scripts for automation
│   └── clean_data.py
│
├── assets/         # Saved plots for README
├── requirements.txt
├── README.md
└── LICENSE

## 🛠️ Tech Stack
Python — Pandas, NumPy
Data Visualization — Matplotlib, Seaborn
Database — PostgreSQL/MySQL (SQLAlchemy for connection)
Notebooks — Jupyter Notebook

## 📌 Key Analyses
🔍 Missing Values Analysis — Identify data gaps using a heatmap.
💰 Price Trends — Histogram & group-wise averages.
🌍 Neighbourhood Insights — Distribution of listings by area.
📈 Correlation Study — Relationship between numeric features.

