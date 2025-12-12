import os
import pandas as pd

RAW_DIR = os.path.join("data", "raw")

# list all csv in raw folder
files = [f for f in os.listdir(RAW_DIR) if f.endswith(".csv")]

print("Counting data samples...\n")

for file in files:
    path = os.path.join(RAW_DIR, file)
    df = pd.read_csv(path)

    print(f"{file}: {len(df):,} rows")

print("\nDone.")