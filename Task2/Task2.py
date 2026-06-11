import pandas as pd
import requests
import os

s4= pd.read_excel("../Python_test_file_material.xlsx", sheet_name="Sheet4")

os.makedirs("images",exist_ok=True)

for index, row in s4.iterrows():
    url= row["urls"]

    if pd.notna(url):
        response = requests.get(url)

        if response.status_code==200:
            filename = f"image_{index+1}.jpg"
            filepath = os.path.join("images", filename)

            with open(filepath, "wb") as file:
                file.write(response.content)
