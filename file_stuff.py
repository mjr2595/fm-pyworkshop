import json
from pprint import pprint

with open("cities.json") as f:
    data = json.load(f)
    print(data)

pprint(data)
