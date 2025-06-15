# Imports
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Local Libraries
from data import data


# Define the URL
url = data.get_dataset_path("rbs", "urls", "red_blue_states_url", 1)
response = requests.get(url)

webpage = BeautifulSoup(response.text, "lxml")
print("Title of the web page: ", webpage.title.string)

# Getting the table
tables = webpage.find_all(name="table", attrs={"class": "wikitable"})

print("Number of tables where class name is 'wikitable': ", len(tables))

table = tables[0]

# Get Columns
headers = table.find_all(name="th")

columns = [column.text.strip() for column in headers[:-1]]

print("Table columns are: \n", columns)

# Body
body = table.find_all(name="tr")


winner_contents = []

for row_id in range(2, 4):
    row_data = []
    for data in body[row_id].find_all("td"):
        # Parties name.
        if data.find("span"):
            row_data.append(data.text.strip())
            continue

        # Candidates name.
        b_tag = data.find("b")

        if b_tag:
            row_data.append(b_tag.text.replace("\n", "").strip())
        else:
            row_data.append(None)

    winner_contents.append({column: value for column, value in zip(columns, row_data)})

print("View the first row of the winner_contents: ", winner_contents[0])
print("\nView the second row of the winner_contents: ", winner_contents[-1])


winner_dataframe = pd.DataFrame(data=winner_contents, columns=columns)
print(winner_dataframe)