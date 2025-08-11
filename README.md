# 🏙️ New York City Airbnb Data Analysis

## 📌 Project Overview
This project analyzes the **New York City Airbnb Open Data** to uncover insights about pricing, availability, and customer engagement.  
It involves **data cleaning**, **exploratory data analysis (EDA)**, **advanced analysis**, and **visualization** using Python.  
The goal is to explore how factors like **number of reviews**, **price**, and **availability** relate to each other and to identify patterns in the NYC Airbnb market.

---

## 📂 Repository Structure
```
NYC_Airbnb_Analysis/
│── Dataset.csv                               # Airbnb dataset used for analysis
│── nyc_airbnb.py                             # Python script for analysis
│── New York City Airbnb Data Analysis Report.pdf   # Detailed project report (PDF format)
```


---

## 🛠️ Tools & Libraries Used
- **Python** (Pandas, NumPy, Matplotlib, Seaborn)  
- **Jupyter/VS Code** for development  
- **MS Word / PDF** for project report  

---

## 📊 Key Analysis Steps
1. **Data Cleaning**  
   - Checked for missing values and handled them appropriately.  
   - Detected and treated outliers using IQR.  

2. **Exploratory Data Analysis (EDA)**  
   - Scatter plots for relationships between `number_of_reviews`, `price`, and `availability_365`.  
   - Histograms and boxplots for distribution insights.  
   - Grouped analysis by `room_type` and `neighbourhood_group`.  

3. **Advanced Analysis**  
   - Applied statistical correlation analysis.  
   - Investigated patterns across different neighborhoods.  

4. **Visualization**  
   - Created clear and visually appealing charts using Matplotlib & Seaborn.  

---

## 📌 Key Insights
- Certain neighborhoods and room types have significantly higher average prices.  
- Listings with **moderate pricing** tend to receive more reviews.  
- Seasonal availability plays a role in price variations.  

---

## 📑 Files Description
- **Dataset.csv** – Source dataset from [Kaggle](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data).  
- **nyc_airbnb.py** – Main Python analysis script.  
- **New York City Airbnb Data Analysis Report.docx / .pdf** – Full report with detailed analysis and visualizations.  

---

## 🚀 How to Run the Project
```bash
# Clone the repository
git clone https://github.com/YourUsername/NYC_Airbnb_Analysis.git

# Navigate to the project folder
cd NYC_Airbnb_Analysis

# Install required libraries
pip install pandas numpy matplotlib seaborn

# Run the analysis script
python nyc_airbnb.py.

````

---

## 📷 Example Visualizations

1. **Price vs. Number of Reviews** <img width="1228" height="878" alt="image" src="https://github.com/user-attachments/assets/17c3b15a-142f-43f5-84cf-a1db6c1717d5" />

2. **Average Availability by Room Type** <img width="1266" height="896" alt="image" src="https://github.com/user-attachments/assets/6df6b816-29e6-4c76-b247-9d27170161e2" />

3. **Top Neighborhoods by Listings** <img width="1181" height="834" alt="image" src="https://github.com/user-attachments/assets/04f27f83-af8c-4cec-86a5-c50d96b31b06" />

---

## 📜 License

This project is licensed under the MIT License.

---

## ✍️ Author

**AFNAN MADI**
Business Intelligence Analyst | Data Enthusiast
[LinkedIn](https://www.linkedin.com/in/afnan-madi) | [GitHub](https://github.com/Afnanmadi/NYC_Airbnb_Analysis)

```


