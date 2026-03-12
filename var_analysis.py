import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Create folders if they don't exist
os.makedirs("data", exist_ok=True)
os.makedirs("results", exist_ok=True)

# Download stock data
ticker = "AAPL"
data = yf.download(ticker, start="2018-01-01")

prices = data["Close"]
returns = prices.pct_change().dropna()

# Save dataset
returns.to_csv("data/returns.csv")

# Portfolio value
portfolio_value = 100000

# Historical VaR
var_95 = np.percentile(returns, 5) * portfolio_value

# Parametric VaR
mu = returns.mean()
sigma = returns.std()

z_score = -1.65
parametric_var = (mu + z_score * sigma) * portfolio_value

print("Historical VaR (95%):", var_95)
print("Parametric VaR (95%):", parametric_var)

# Plot return distribution
plt.figure(figsize=(10,6))
plt.hist(returns, bins=50)

plt.axvline(np.percentile(returns,5), linestyle="dashed")

plt.title("Distribution of Daily Returns")
plt.xlabel("Returns")
plt.ylabel("Frequency")

plt.savefig("results/return_distribution.png")

plt.show()