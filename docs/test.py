from urllib.request import urlopen
import json
import pandas as pd
from pprint import pprint

from data import data


# Collect the data
path = data.get_dataset_path("rbs", "processed", "us_presidential_elections_by_state_and_party", 1)
data = pd.read_csv(path)
df = data[1:].copy()
df.rename(columns = {"Year": "State"}, inplace = True)

print(df.head())

# Create FIPS
with urlopen("https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json") as response:
    countries_geojson = json.load(response)

pprint(countries_geojson["features"][0]["properties"]["name"])

print(df.loc("State", 0))