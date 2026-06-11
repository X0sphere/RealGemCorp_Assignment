"""
For 200K rows, I would modify the code like this:
1. Read the file in chunks instead of loading everything at once.
2. Keep only required columns like asin, sku, price, product_description.
3. Convert large repeated text columns into category type where possible.
4. Avoid unnecessary copies of DataFrames.
5. Use chunk-wise merge or database-style processing.
6. Write output incrementally to CSV/TSV instead of holding full output in memory.
7. For very large Excel files, first convert them to CSV and then process using chunks.
8. If data grows beyond Excel limits, use SQLite, DuckDB, or PostgreSQL.
"""

import pandas as pd

s2 = pd.read_excel("../Python_test_file_material.xlsx", sheet_name="Sheet2")
s3 = pd.read_excel("../Python_test_file_material.xlsx", sheet_name="Sheet3")

s3_lookup = s3.set_index("asin")

chunk_size = 50000

for i in range(0, len(s2), chunk_size):
    chunk = s2.iloc[i:i + chunk_size]

    merged_chunk = chunk.merge(
        s3,
        on="asin",
        how="left"
    )

    merged_chunk.to_csv(
        "large_output.csv",
        mode="a",
        index=False,
        header=(i == 0)
    )