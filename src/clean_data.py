import os
import pandas as pd

# --------------------------------------------------
# 1. Locate important folders
# --------------------------------------------------

THIS_FILE = os.path.abspath(__file__)
SRC_DIR = os.path.dirname(THIS_FILE)
PROJECT_DIR = os.path.dirname(SRC_DIR)

# Folders for raw (input) and processed (output) data
RAW_DIR = os.path.join(PROJECT_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(PROJECT_DIR, "data", "processed")

# Create processed folder 
os.makedirs(PROCESSED_DIR, exist_ok=True)

print("Reading raw data from   :", RAW_DIR)
print("Saving cleaned data to  :", PROCESSED_DIR)

# --------------------------------------------------
# 2. List all raw CSV files
# --------------------------------------------------

raw_files = [f for f in os.listdir(RAW_DIR) if f.endswith("_raw.csv")]

if not raw_files:
    raise FileNotFoundError(
        f"No *_raw.csv files found in {RAW_DIR}. "
        "Make sure get_data.py has downloaded the data."
    )

# --------------------------------------------------
# 3. Clean each raw file
# --------------------------------------------------

for filename in sorted(raw_files):
    raw_path = os.path.join(RAW_DIR, filename)
    print(f"\nCleaning raw file: {filename} ...")

    # Read raw CSV normally (use header row in the file)
    df = pd.read_csv(raw_path)

    # Show columns for debugging
    print("  Columns:", list(df.columns))

    # ------------------------------------
    # 3.1 Make sure we have a Date column
    # ------------------------------------
    if "Date" not in df.columns:
        # If there is no 'Date' column, we assume the FIRST column is the date.
        # In the files this column is called 'Price', but it actually stores dates.
        first_col = df.columns[0]
        print(
            f"  'Date' column not found. Assuming '{first_col}' "
            "is the date column and renaming it to 'Date'."
        )
        df = df.rename(columns={first_col: "Date"})

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Drop rows where Date could not be parsed
    before_drop = len(df)
    df = df.dropna(subset=["Date"])
    after_drop = len(df)
    print(f"  Dropped {before_drop - after_drop} rows with invalid dates.")

    # ------------------------------------
    # 3.2 Drop columns we do not need
    # ------------------------------------
    # If there is a Ticker column, drop it (not needed for this project)
    if "Ticker" in df.columns:
        df = df.drop(columns=["Ticker"])

    # We only keep Date and Close price for the analysis
    if "Close" not in df.columns:
        raise ValueError(f"'Close' column not found in {filename}")

    df = df[["Date", "Close"]]

    # Reset index to 0, 1, 2, ...
    df = df.reset_index(drop=True)

    # ------------------------------------
    # 3.3 Save cleaned file
    # ------------------------------------
    processed_name = filename.replace("_raw", "_processed")
    save_path = os.path.join(PROCESSED_DIR, processed_name)
    df.to_csv(save_path, index=False)

    print(f"  Saved cleaned file → {save_path}")

print("\nAll files cleaned and saved in data/processed/")