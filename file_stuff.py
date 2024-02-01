import json
from pprint import pprint


with open("cities.json", encoding="utf-8") as f:
    data = json.load(f)
    print(data)

pprint(data)
