# DSCI 510 – Final Project (Fall 2025) – Analyzing Key Factors Influencing Volatility in Major Technology Stocks: AAPL, MSFT, NVDA, TSLA and AMZN

## Author
```text
Aphinya Chokwareephorn
USCID: 9637644926
Email: chokware@usc.edu
```

## Project Summary
This project analyzes volatility patterns in five major technology stocks—Apple (AAPL), Microsoft (MSFT), NVIDIA (NVDA), Tesla (TSLA), and Amazon (AMZN)—using historical daily market data from 2021 to 2025.

Key analyses include:
- Daily returns
- Distribution of returns
- 30-day rolling volatility
- Annualized volatility
- Correlation across stocks

The goal is to compare risk profiles, identify high-volatility periods, and understand how these assets behave relative to one another. The project uses fully automated data collection via the yfinance library.
---

## 1. Repository Structure
```text
DSCI510_final_project/
├── data/
│   ├── raw/
│   │   ├── AAPL_raw.csv
│   │   ├── AMZN_raw.csv
│   │   ├── MSFT_raw.csv
│   │   ├── NVDA_raw.csv
│   │   └── TSLA_raw.csv
│   └── processed/
│       ├── AAPL_processed.csv
│       ├── AMZN_processed.csv
│       ├── MSFT_processed.csv
│       ├── NVDA_processed.csv
│       ├── TSLA_processed.csv
│       └── stocks_clean.csv
├── results/
│   ├── daily_returns.csv
│   ├── rolling_volatility_30d.csv
│   ├── annualized_volatility.csv
│   ├── returns_correlation.csv
│   ├── sorted_volatility.csv
│   ├── plot_prices.png
│   ├── plot_rolling_volatility_30d.png
│   ├── plot_annualized_volatility.png
│   ├── plot_daily_returns_distribution.png
│   └── plot_returns_correlation_heatmap.png
├── src/
│   ├── get_data.py
│   ├── clean_data.py
│   ├── run_analysis.py
│   ├── visualize_results.py
│   └── count_rows.py
├── Final_Report.pdf
├── Project_Proposal.pdf
├── README.md
└── requirements.txt
```

## 2. Setup Instructions
It is recommended to run the project inside a virtual environment to keep dependencies clean.

1. Create Virtual Environment
### **Mac / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

Your terminal should show (.venv) when activated.

## 2. Install Dependencies
The project uses five packages:
- yfinance
- pandas
- numpy
- matplotlib
- seaborn

Install them with:
```bash
pip install -r requirements.txt
```

## 3. How to Run the Project
Below is the complete workflow used in this project.

### **Step 1 — Download Stock Data**
This retrieves daily closing prices & trading volume (2021–2025) from Yahoo Finance.
```bash
python src/get_data.py
```

Saves files like:
data/raw/AAPL_raw.csv, data/raw/MSFT_raw.csv, etc.

### **Step 2 — Clean and Prepare the Data**
This script:
- Converts dates
- Fixes missing or invalid rows
- Keeps only useful columns (Date, Close)
- Aligns all stocks by trading date
- Saves clean datasets

Run:
```bash
python src/clean_data.py
```

Outputs are saved to:
data/processed/*_processed.csv

### **Step 3 — Run Analysis**
This script computes:
- Daily returns
- 30-day rolling volatility
- Annualized volatility
- Correlation matrix
- Creates stocks_clean.csv

Run:
```bash
python src/run_analysis.py
```

Files are saved in /results/.

### **Step 4. Generate Visualizations**
Creates all charts used in the report:
- Stock Price History
- Rolling Volatility (30-Day)
- Daily Return Distribution
- Annualized Volatility (Bar Chart)
- Correlation Heatmap

Run:
```bash
python src/visualize_results.py
```

Plots are saved in /results/*.png.

## 4. Analyses Performed
- Daily Returns – percentage change in closing prices
- Distribution of Returns – histogram + KDE for risk comparison
- Rolling Volatility (30-day) – short-term risk dynamics
- Annualized Volatility – long-term risk ranking
- Correlation Matrix – relationships across stocks

## 5.Key Findings (Summary)
- TSLA and NVDA show the highest volatility (short-term and long-term).
- MSFT and AAPL remain consistently stable.
- AMZN sits in the middle of the volatility spectrum.
- Correlations range 0.42–0.65, indicating moderate shared movement but also diversification value—especially from TSLA.

## 6. Future Work
- Apply predictive modeling (ARIMA, GARCH, LSTM).
- Expand dataset across sectors for cross-industry comparison.

## Instructor Submission Notes
This repository contains:
- Full project code
- Data pipeline
- Analysis results
- Final written report (PDF)