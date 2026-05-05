import pandas as pd
import os

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

print("Loading data...")
df = pd.read_parquet("data/sample_data.parquet")

print("Processing data...")
df["revenue"] = df["price"] * df["qty"]

# Compute summary
summary = df.groupby("category").agg(
    total_revenue=("revenue", "sum"),
    total_quantity=("qty", "sum"),
    avg_price=("price", "mean")
).reset_index()

print("Saving report...")
summary.to_csv("output/report.csv", index=False)

print("✅ Report generated at output/report.csv")
