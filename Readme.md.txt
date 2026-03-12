# Value-at-Risk (VaR) Analysis

This project implements **Value-at-Risk (VaR)** techniques to measure the downside risk of a stock portfolio using historical market data.

---

### 📊 Key Results

- Calculated **Historical Value-at-Risk (VaR)** at 95% confidence level  
- Estimated **Parametric VaR** using the normal distribution assumption  
- Visualized the **distribution of daily returns**  

---

### 🛠️ Technology Stack

- Python  
- pandas  
- numpy  
- matplotlib  
- yfinance  

---

### 💾 Dataset

- Daily stock prices downloaded from Yahoo Finance  
- Example ticker: **AAPL**  
- Data period: 2018–Present  

Saved as:
data/returns.csv


---

### 📈 Output

Distribution of daily returns:

![Return Distribution](results/return_distribution.png)

The dashed vertical line represents the **95% VaR threshold**, indicating potential downside risk.

---

### ⚡ How to Run

1️⃣ Install dependencies

pip install -r requirements.txt

2️⃣ Run the script


python var_analysis.py


3️⃣ Generated outputs


data/returns.csv
results/return_distribution.png


---

### 🎯 Key Takeaways

- Value-at-Risk quantifies the **maximum expected loss** over a given time horizon  
- Historical VaR relies on **empirical return distribution**  
- Parametric VaR assumes **normal distribution of returns**  

This project demonstrates how **financial risk theory can be implemented with Python for practical portfolio risk management**.
