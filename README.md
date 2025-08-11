# NYC_Airbnb_Analysis

End-to-end analysis of the **New York City Airbnb Open Data** to explore how the **number of reviews** relates to **price**, **availability**, and listing features. This project covers **data cleaning**, **EDA**, **visualization**, and a light **predictive exploration**, delivered in a reproducible Python workflow.

> **Goal:** Translate raw Airbnb data into clear, decision-ready insights and visuals.

---

## 🔍 Key Questions
1. How does **number_of_reviews** relate to **price** and **availability_365**?
2. Do relationships differ by **room_type** or **neighbourhood_group**?
3. What outliers exist (e.g., extreme prices) and how do they affect insights?

---

## 🧰 Tech Stack
- **Python**: `pandas`, `numpy`
- **Visualization**: `matplotlib`, `seaborn`
- **Environment**: Jupyter / Google Colab

---

## 📦 Project Structure
```
NYC_Airbnb_Analysis/
├─ data/
│  └─ AB_NYC_2019.csv           # (add locally or access via Kaggle link)
├─ notebooks/
│  └─ 01_nyc_airbnb_eda.ipynb   # cleaning + EDA + visuals
├─ src/
│  ├─ cleaning.py               # helper functions for NA/outliers
│  └─ viz.py                    # helper functions for charts
├─ outputs/
│  ├─ figures/                  # exported charts
│  └─ summary/                  # brief findings (md/pdf)
├─ README.md
└─ requirements.txt
```

> You can start with just `notebooks/01_nyc_airbnb_eda.ipynb` and add `/src` helpers later.

---

## 🗂 Dataset
- **Source:** Kaggle – NYC Airbnb Open Data: https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data
- **File:** `AB_NYC_2019.csv`
- **Key fields:** `price`, `availability_365`, `number_of_reviews`, `room_type`, `neighbourhood_group`, `latitude`, `longitude`

> **Note:** Do not commit large/raw data. Keep it local or add to `.gitignore`.

---

## ⚙️ Setup & Run

### 1) Create environment
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

**requirements.txt**
```
pandas
numpy
matplotlib
seaborn
jupyter
```

### 3) Launch notebook
```bash
jupyter notebook notebooks/01_nyc_airbnb_eda.ipynb
```

---

## 🔧 Methodology

### A. Data Cleaning
- Inspect structure with `df.info()` / `df.describe()`
- Handle missing values (drop or `fillna` as appropriate)
- Detect & treat outliers (e.g., IQR on `price`)
- Type casting (dates/numerics if needed)

### B. Exploratory Analysis
- Descriptive stats for `price`, `number_of_reviews`, `availability_365`
- Correlations and pairwise relationships
- Grouped comparisons by `room_type` and `neighbourhood_group`

### C. Visualization
- **Scatter plots**: reviews vs price / availability
- **Boxplots**: price by room type / neighbourhood group
- **Histograms**: distributions of key metrics
- **Heatmaps** (optional): correlations

### D. (Optional) Predictive Exploration
- Simple baseline regressions or trend lines to check associations
- Clear caveats: correlation ≠ causation

---

## 📊 Key Findings (Template – replace with your results)
- Listings with **moderate prices** tend to receive **more reviews** than very high-priced listings.
- **Entire home/apt** listings are **higher-priced** but often have **fewer reviews** than private rooms.
- Some neighbourhood groups show **distinct price bands** and **review volumes**.
- Outliers (e.g., extreme prices) can distort averages; trimming improves stability.

> Add 1–2 screenshots of your charts in `outputs/figures/` and embed below.

---

## 🖼 Example Visuals (add your images)
```markdown
![Scatter: Reviews vs Price](outputs/figures/reviews_vs_price.png)
![Boxplot: Price by Room Type](outputs/figures/price_by_room_type.png)
```

---

## 🧭 Reproducibility Notes
- Random seeds (if used) should be fixed for repeatable results.
- Document thresholds used for outlier handling (e.g., 1.5×IQR).

---

## 📜 Ethics & Limits
- Findings describe **associations**, not causation.
- Prices and reviews are influenced by seasonality, marketing, and host behavior not captured here.

---

## 📣 Acknowledgments
- Dataset: **Kaggle – NYC Airbnb Open Data**
- Coursework: **Willis College – Business Intelligence Analysis**
