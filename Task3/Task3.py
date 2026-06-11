import pandas as pd

# Create products
products = pd.DataFrame({
    "asin": ["A1", "A2", "A3"],
    "sku": ["SKU1", "SKU2", "SKU3"]
})

products.to_excel("Products.xlsx", index=False)


# Create parent_child
parent_child = pd.DataFrame({
    "parent_asin": ["P1", "P1", "P2"],
    "asin": ["A1", "A2", "A3"]
})

parent_child.to_excel("Parent_child.xlsx", index=False)


# Read parent_child
df = pd.read_excel("Parent_child.xlsx")


# Count child asinss for each parent asin
output = (
    df.groupby("parent_asin")
      .size()
      .reset_index(name="child_count")
)


# Save output
output.to_excel("Task3_output.xlsx", index=False)
output.to_csv("Task3_output.csv", index=False)

# print(output)