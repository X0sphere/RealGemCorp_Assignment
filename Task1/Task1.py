import pandas as pd

s2 = pd.read_excel("../Python_test_file_material.xlsx", sheet_name="Sheet2")
s3 = pd.read_excel("../Python_test_file_material.xlsx", sheet_name="Sheet3")

merge = s2.merge(s2, on="asin", how="left")

merge.to_excel("Task1_output.xlsx", index=False)
merge.to_csv("Task1_output.csv", index=False)
merge.to_csv("Task1_output.tsv", sep="\t", index=False)
