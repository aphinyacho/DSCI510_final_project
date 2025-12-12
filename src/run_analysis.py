import os
from functools import reduce

import numpy as np
import pandas as pd

# --------------------------------------------------
# 1. Locate important folders
# --------------------------------------------------

THIS_FILE = os.path.abspath(__file__)
SRC_DIR = os.path.dirname(THIS_FILE)
PROJECT_DIR = os.path.dirname(SRC_DIR)

# Folders for processed data and results
PROCESSED_DIR = os.path.join(PROJECT_DIR, "data", "processed")
RESULTS_DIR = os.path.join(PROJECT_DIR, "results")

# Create results folder if it does not exist
os.makedirs(RESULTS_DIR, exist_ok=True)

print("Using processed data from :", PROCESSED_DIR)
print("Saving analysis results to:", RESULTS_DIR)

# --------------------------------------------------
# 2. Load all *_processed.csv files and merge them
# --------------------------------------------------

# Find all processed CSV files like AAPL_processed.csv
processed_files = [
    f for f in os.listdir(PROCESSED_DIR) if f.endswith("_processed.csv")
]

if not processed_files:
    raise FileNotFoundError(
        f"No *_processed.csv files found in {PROCESSED_DIR}. "
        "Make sure clean_data.py has been run."
    )

price_tables = []

for filename in sorted(processed_files):
    file_path = os.path.join(PROCESSED_DIR, filename)
    ticker = filename.split("_")[0]  # e.g. 'AAPL_processed.csv' -> 'AAPL'

    print(f"Loading processed file for {ticker}: {filename}")

    # Read the processed CSV
    df = pd.read_csv(file_path)

    # Make sure we have a Date column
    if "Date" not in df.columns:
        raise ValueError(f"'Date' column not found in {filename}")

    # Parse Date column
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])

    # Keep only Date and Close, rename Close -> ticker
    if "Close" not in df.columns:
        raise ValueError(f"'Close' column not found in {filename}")

    sub = df[["Date", "Close"]].rename(columns={"Close": ticker})
    price_tables.append(sub)

# Merge all tickers on Date using inner join
prices = reduce(
    lambda left, right: pd.merge(left, right, on="Date", how="inner"),
    price_tables,
)

# Sort by Date and set Date as index
prices = prices.sort_values("Date").set_index("Date")

# Convert all columns to numeric
prices = prices.apply(pd.to_numeric, errors="coerce").dropna(how="all")

print("\nMerged price table shape:", prices.shape)
print("Columns (tickers):", list(prices.columns))

# Save combined clean price table
combined_path = os.path.join(PROCESSED_DIR, "stocks_clean.csv")
prices.to_csv(combined_path)
print(f"Saved combined clean prices to: {combined_path}")

# --------------------------------------------------
# 3. Compute daily returns
# --------------------------------------------------

daily_returns = prices.pct_change().dropna()
print("\nDaily returns shape:", daily_returns.shape)

daily_returns_path = os.path.join(RESULTS_DIR, "daily_returns.csv")
daily_returns.to_csv(daily_returns_path)
print(f"Saved daily returns to: {daily_returns_path}")

# --------------------------------------------------
# 4. 30-day rolling volatility 
# --------------------------------------------------

ROLLING_WINDOW = 30  # days

rolling_vol = daily_returns.rolling(window=ROLLING_WINDOW).std()

rolling_vol_path = os.path.join(RESULTS_DIR, "rolling_volatility_30d.csv")
rolling_vol.to_csv(rolling_vol_path)
print(f"Saved 30-day rolling volatility to: {rolling_vol_path}")

# --------------------------------------------------
# 5. Annualized volatility per stock
# --------------------------------------------------

TRADING_DAYS = 252  # typical number of trading days in a year

daily_std = daily_returns.std()
annualized_vol = daily_std * np.sqrt(TRADING_DAYS)
annualized_vol_df = annualized_vol.to_frame(name="Annualized_Volatility")

ann_vol_path = os.path.join(RESULTS_DIR, "annualized_volatility.csv")
annualized_vol_df.to_csv(ann_vol_path)
print(f"Saved annualized volatility to: {ann_vol_path}")

print("\nAnnualized volatility:")
print(annualized_vol_df)

# --------------------------------------------------
# 6. Correlation matrix of returns
# --------------------------------------------------

corr_matrix = daily_returns.corr()

corr_path = os.path.join(RESULTS_DIR, "returns_correlation.csv")
corr_matrix.to_csv(corr_path)
print(f"\nSaved correlation matrix to: {corr_path}")

print("\nCorrelation matrix:")
print(corr_matrix)

# --------------------------------------------------
# 7. Sort stocks by risk (annualized volatility)
# --------------------------------------------------

sorted_vol = annualized_vol_df.sort_values(
    "Annualized_Volatility", ascending=False
)

sorted_vol_path = os.path.join(RESULTS_DIR, "sorted_volatility.csv")
sorted_vol.to_csv(sorted_vol_path)
print(f"\nSaved sorted volatility to: {sorted_vol_path}")

print("\nStocks sorted by annualized volatility (highest risk first):")
print(sorted_vol)

print("\nAnalysis completed.")