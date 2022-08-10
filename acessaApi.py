import requests
import json
import pandas as pd

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://randomuser.me/api/?results=10")

pf = pd.DataFrame.from_dict(response.json(), orient="index")

jprint(response.json())

pf.to_csv('out.csv')  