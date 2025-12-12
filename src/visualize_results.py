import os
import traceback

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

try:
    # --------------------------------------------------
    # 1. Locate important folders
    # --------------------------------------------------
    
    THIS_FILE = os.path.abspath(__file__)
    SRC_DIR = os.path.dirname(THIS_FILE)
    PROJECT_DIR = os.path.dirname(SRC_DIR)

    PROCESSED_DIR = os.path.join(PROJECT_DIR, "data", "processed")
    RESULTS_DIR = os.path.join(PROJECT_DIR, "results")

    print("Reading processed data from :", PROCESSED_DIR)
    print("Reading analysis results from:", RESULTS_DIR)

    # Make sure the results folder exists
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # --------------------------------------------------
    # 2. Load data for visualization
    # --------------------------------------------------
    prices_path = os.path.join(PROCESSED_DIR, "stocks_clean.csv")
    daily_returns_path = os.path.join(RESULTS_DIR, "daily_returns.csv")
    rolling_vol_path = os.path.join(RESULTS_DIR, "rolling_volatility_30d.csv")
    annual_vol_path = os.path.join(RESULTS_DIR, "annualized_volatility.csv")
    corr_path = os.path.join(RESULTS_DIR, "returns_correlation.csv")

    print("\nLoading files:")
    print("  ", prices_path)
    print("  ", daily_returns_path)
    print("  ", rolling_vol_path)
    print("  ", annual_vol_path)
    print("  ", corr_path)

    # Important: parse the Date column as datetime and use it as index
    prices = pd.read_csv(prices_path, parse_dates=["Date"], index_col="Date")
    daily_returns = pd.read_csv(daily_returns_path, parse_dates=["Date"], index_col="Date")
    rolling_vol = pd.read_csv(rolling_vol_path, parse_dates=["Date"], index_col="Date")

    # These two do not need Date index
    annualized_vol = pd.read_csv(annual_vol_path, index_col=0)
    corr_matrix = pd.read_csv(corr_path, index_col=0)

    print("\nData loaded for visualization.")
    print("Price columns        :", list(prices.columns))
    print("Daily returns columns:", list(daily_returns.columns))

    # --------------------------------------------------
    # 3. Set basic plot style
    # --------------------------------------------------
    sns.set_theme(style="whitegrid")

    # --------------------------------------------------
    # 4. Plot 1: Stock price history
    # --------------------------------------------------
    plt.figure(figsize=(10, 6))
    for ticker in prices.columns:
        # x-axis = prices.index (Date), y-axis = price values
        plt.plot(prices.index, prices[ticker], label=ticker)

    plt.title("Stock Price History (2021–2025)")
    plt.xlabel("Date")
    plt.ylabel("Price (Close)")
    plt.legend()
    plt.tight_layout()

    price_plot_path = os.path.join(RESULTS_DIR, "plot_prices.png")
    plt.savefig(price_plot_path)
    plt.close()
    print(f"Saved price history plot to: {price_plot_path}")

    # --------------------------------------------------
    # 5. Plot 2: 30-day rolling volatility
    # --------------------------------------------------
    plt.figure(figsize=(10, 6))
    for ticker in rolling_vol.columns:
        plt.plot(rolling_vol.index, rolling_vol[ticker], label=ticker)

    plt.title("30-Day Rolling Volatility (Daily Returns)")
    plt.xlabel("Date")
    plt.ylabel("Rolling Std Dev (30 days)")
    plt.legend()
    plt.tight_layout()

    rolling_plot_path = os.path.join(RESULTS_DIR, "plot_rolling_volatility_30d.png")
    plt.savefig(rolling_plot_path)
    plt.close()
    print(f"Saved rolling volatility plot to: {rolling_plot_path}")

    # --------------------------------------------------
    # 6. Plot 3: Annualized volatility (bar chart)
    # --------------------------------------------------
    plt.figure(figsize=(8, 5))
    annualized_vol["Annualized_Volatility"].plot(kind="bar")

    plt.title("Annualized Volatility by Stock")
    plt.xlabel("Stock")
    plt.ylabel("Annualized Volatility")
    plt.tight_layout()

    annual_vol_plot_path = os.path.join(RESULTS_DIR, "plot_annualized_volatility.png")
    plt.savefig(annual_vol_plot_path)
    plt.close()
    print(f"Saved annualized volatility bar chart to: {annual_vol_plot_path}")

    # --------------------------------------------------
    # 7. Plot 4: Correlation heatmap of daily returns
    # --------------------------------------------------
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", square=True, cmap="coolwarm")

    plt.title("Correlation of Daily Returns")
    plt.tight_layout()

    corr_plot_path = os.path.join(RESULTS_DIR, "plot_returns_correlation_heatmap.png")
    plt.savefig(corr_plot_path)
    plt.close()
    print(f"Saved correlation heatmap to: {corr_plot_path}")

    # --------------------------------------------------
    # 8. Plot 5: Distribution of daily returns
    # --------------------------------------------------
    plt.figure(figsize=(10, 6))

    for ticker in daily_returns.columns:
        sns.histplot(
            daily_returns[ticker],
            bins=50,
            kde=True,
            stat="density",
            element="step",
            label=ticker,
            alpha=0.4,
        )

    plt.title("Distribution of Daily Returns")
    plt.xlabel("Daily Return")
    plt.ylabel("Density")
    plt.legend()
    plt.tight_layout()

    returns_dist_plot_path = os.path.join(RESULTS_DIR, "plot_daily_returns_distribution.png")
    plt.savefig(returns_dist_plot_path)
    plt.close()
    print(f"Saved daily returns distribution plot to: {returns_dist_plot_path}")

    print("\nAll visualizations created and saved in the results/ folder.")

except Exception as e:
    print("\nError while running visualize_results.py")
    print(e)
    traceback.print_exc()