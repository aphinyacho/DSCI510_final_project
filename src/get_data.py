import yfinance as yf
import os

# --------------------------------------------------
# 1. Find the project root folder
# --------------------------------------------------

THIS_FILE = os.path.abspath(__file__)
SRC_DIR = os.path.dirname(THIS_FILE)
PROJECT_DIR = os.path.dirname(SRC_DIR)   # go up one folder

# --------------------------------------------------
# 2. Define paths
# --------------------------------------------------
RAW_DIR = os.path.join(PROJECT_DIR, "data", "raw")

# Create the directory if missing
os.makedirs(RAW_DIR, exist_ok=True)

# --------------------------------------------------
# 3. Settings
# --------------------------------------------------
tickers = ["AAPL", "MSFT", "NVDA", "TSLA", "AMZN"]
start_date = "2021-01-01"
end_date = "2025-12-31"

# --------------------------------------------------
# 4. Download each ticker
# --------------------------------------------------
for ticker in tickers:
    print(f"Downloading data for {ticker}...")

    df = yf.download(ticker, start=start_date, end=end_date)

    save_path = os.path.join(RAW_DIR, f"{ticker}_raw.csv")
    df.to_csv(save_path)

    print(f"Saved {ticker} → {save_path}")

print("\nAll downloads completed successfully!")