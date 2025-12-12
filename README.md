# Final Project – Analyzing Key Factors Influencing Volatility in Major Technology Stocks: AAPL, MSFT, NVDA, TSLA and AMZN

## Author
Aphinya Chokwareephorn
USCID: 9637644926
Email: chokware@usc.edu
DSCI 510 – Final Project (Fall 2025)

This project analyzes volatility patterns in five major technology stocks—AAPL, MSFT, NVDA, TSLA, and AMZN—using historical daily data from January 2021 to December 2025. The workflow retrieves raw data programmatically, processes and cleans the datasets, performs quantitative analysis, and generates visualizations to compare risk profiles across companies.

## Project Overview
Technology stocks vary significantly in price stability, risk exposure, and response to market conditions.
This project investigates:
- How volatility differs among major tech stocks 
- How these volatility patterns evolve over time 
- Which stocks are most stable vs. most volatile
- How correlations reveal shared market behavior

The analysis combines daily returns, rolling volatility, annualized volatility, return distributions, and correlation matrices to assess each company’s risk profile.
---

## 1. Virtual Environment Setup
It is recommended to run the project inside a virtual environment to keep dependencies clean.

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

## 3. Project Structure
DSCI510_final_project/
│
├── data/
│   ├── processed/
│   └── raw/
│
├── results/
│
├── src/
│   ├── clean_data.py
│   ├── count_rows.py
│   ├── get_data.py
│   └── visualize_results.py
│
├── Final_Report.pdf
├── Project_Proposal.pdf
├── README.md
└── requirements.txt

## 4. How to Run the Project
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

## 5. Data Retrieval Method
The project uses the yfinance Python library, which:
- programmatically retrieves historical daily stock data from Yahoo Finance
- returns the data directly as Pandas DataFrames
- allows the data to be saved as CSV files using Python scripts

This enables a fully automated and reproducible data collection process without manual downloads.

## 6.Data Cleaning Process
The cleaning script ensures:
- all tickers share the same date index
- missing data is handled (drop or forward-fill)
- columns are standardized
- one combined DataFrame is created for analysis

This step prepares the dataset for stable and accurate calculations.

## 7. Analysis Performed
The analysis includes:
- daily return calculation
- 30-day rolling volatility
- annualized volatility per stock
- correlation analysis
- comparison of stable vs. high-volatility stocks
- identification of volatility spikes and related events 

## 8. Visualizations Generated
The visual output includes:
- multi-stock price line chart
- rolling volatility plot
- correlation heatmap
- return distribution plots
- bar chart comparing average annualized volatility

These graphs help explain volatility differences among tech companies.