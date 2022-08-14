import requests
import json
import pandas as pd
import re
import phonenumbers
import csv
import io

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def phone_format(phone_number):
    clean_phone_number = re.sub('[^0-9]+', '', phone_number)
    formatted_phone_number = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(clean_phone_number[:-1])) + clean_phone_number[-1]
    return formatted_phone_number

def getData(linhas):
    #dados = requests.get("https://randomuser.me/api/?results="+str(linhas)).content
    url = "https://randomuser.me/api/?format=csv&nat=br&results="+str(linhas)
    meuDataframe = pd.read_csv(url, encoding='latin_1') 
    return meuDataframe

#def formataPhone(meuDataframe):
#    for row in meuDataframe:


dataframeNomes = getData(10)
print(dataframeNomes["cell"])


#dadosJson = dados.json()['results']

#cellNumber = dadosJson[0]['cell']
#i=0
#for row in dadosJson:
#    cellNumber = dadosJson[i]['cell'] 
#    clean_phone_number = re.sub('[^0-9]+', '', cellNumber)

#    numero = phonenumbers.format_number(clean_phone_number,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
#    print(numero)
#    i+=1

    
