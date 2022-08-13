import requests
import json
import pandas as pd
import re

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def phone_format(phone_number):
    clean_phone_number = re.sub('[^0-9]+', '', phone_number)
    formatted_phone_number = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(clean_phone_number[:-1])) + clean_phone_number[-1]
    return formatted_phone_number

def transformaFormatos(meuDataframe):
    meuDataframe['cell'] = phone_format(meuDataframe['cell'])
    return meuDataframe

def formatPhone(number):    
    return('(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', number)))

response = requests.get("https://randomuser.me/api/?results=3")
x = response.json()
df = pd.DataFrame(x['results'])
#novoDf = transformaFormatos(df)
#print(df['cell'])

#print(formatPhone(df['cell'].item()))
print(df['cell'])

#df.to_csv('out.csv')

#pf = pd.DataFrame.from_dict(response.json(), orient="index")

#jprint(response.json()['results'])

#pf.to_csv('out.csv')