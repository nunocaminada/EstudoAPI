import pandas as pd
import time
import re

# Dificuldades: 
# encoding da API, em especial dos dados que não eram BR
# encoding dos arquivos
# dualidade csv/json, que apreta diferenças no tratamento que nem sempre ficam claras na documentação

#Objetivo: Buscar um número determinado de linhas da API Randomuser em formato CSV
#Parametro: número de linhas a retornar no dataframe
#Retorno: Pandas dataframe
def getData(linhas):
    linhas +=1 #para compensar o header
    url = "https://randomuser.me/api/?format=csv&nat=us,br,ca,fr,au&include=name&results="+str(linhas)
    meuDataframe = pd.read_csv(url, encoding='utf-8')
    return meuDataframe

#Objetivo: Escrever arquivo com dados da API Randomuser
#Parametro: Pandas dataframe
#Retorno: nenhum
def escreveResultado(meuDataframe):
    timestampArquivo = time.strftime("%Y%m%d-%H%M%S")
    #print(meuDataframe.head())
    meuDataframe.to_csv('.\\Saida\\'+timestampArquivo+".csv",sep=";",encoding='ansi')

#Objetivo: Converter numeros de celular
#Parametro: Pandas dataframe
#Retorno: Pandas dataframe
def transformaCelulares(meuDataframe):
    meuDataframe['cell'] = meuDataframe['cell'].apply(limpaNumero)
    return meuDataframe

#Objetivo: Limpar caracteres de uma string, deixando apenas numeros
#Parametro: string
#Retorno: numero
def limpaNumero(numero):
    return (re.sub('[^0-9]+', '', numero))

def calculaPorcentagem(meuDataframe):
    quantidadePaises = meuDataframe['location.country'].value_counts()
    print(quantidadePaises)

dataframeNomes = getData(600)
cellLimpos = transformaCelulares(dataframeNomes)

escreveResultado(cellLimpos)

print(cellLimpos['location.country'].describe(include='all'))
print(calculaPorcentagem(cellLimpos))
    
