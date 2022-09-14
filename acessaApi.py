import pandas as pd
import time
import re
import matplotlib.pyplot as plt
import numpy as np
import os

timestampArquivo = time.strftime("%Y%m%d-%H%M%S")
caminhoSaida = '.\\Saida'

# Dificuldades: 
# encoding da API, em especial dos dados que não eram BR
# encoding dos arquivos
# dualidade csv/json, que apresenta diferenças no tratamento que nem sempre ficam claras na documentação

#Objetivo: Buscar um número determinado de linhas da API Randomuser em formato CSV
#Parametro: número de linhas a retornar no dataframe
#Retorno: Pandas dataframe
def getData(linhas):
    linhas +=1 #para compensar o header
    url = "https://randomuser.me/api/?format=csv&nat=us,br,ca,fr,au&results="+str(linhas)
    #le da API e coloca na codificação UTF-8
    meuDataframe = pd.read_csv(url, encoding='utf-8')
    return meuDataframe

#Objetivo: Escrever arquivo com dados da API Randomuser
#Parametro: Pandas dataframe
#Retorno: nenhum
def escreveResultado(meuDataframe):
    #grava um arquivo diferente a cada execução
    meuDataframe.to_csv('.\\Saida\\'+timestampArquivo+".csv",sep=";",encoding='ansi')

#Objetivo: Converter numeros de celular
#Parametro: Pandas dataframe
#Retorno: Pandas dataframe
def transformaCelulares(meuDataframe, coluna):
    meuDataframe[coluna] = meuDataframe[coluna].apply(limpaNumero)
    return meuDataframe

#Objetivo: Limpar caracteres de uma string, deixando apenas numeros
#Parametro: string
#Retorno: numero
def limpaNumero(numero):
    numero =  (re.sub('[^0-9]+', '', numero))
    return format(int(numero[:-1]), ",").replace(",", "-") + numero[-1]

#Objetivo: Imprimir percentual de pessoas por pais e por genero
#Parametro: Dataframe
#Retorno: nenhum
def gravaEstatisticas(meuDataframe):
    #calcula as porcentagens e formata a saída
    porcentagemPaises = ((meuDataframe['location.country'].value_counts()/meuDataframe['location.country'].count())*100).map('{:,.2f}%'.format)
    porcentagemGeneros = ((meuDataframe['gender'].value_counts()/meuDataframe['gender'].count())*100).map('{:,.2f}%'.format)
    #imprime os resultados no terminal para controle
    print("Distribuicao percentual por pais")
    print(porcentagemPaises)
    print("\nDistribuicao percentual por genero")
    print(porcentagemGeneros)
    #grava resultados em arquivo
    f = open('.\\Saida\\'+timestampArquivo+'.txt', "a")
    f.write(str(porcentagemPaises))
    f.write(str(porcentagemGeneros))
    f.close()

#Objetivo: Exibir grafico de distribuição das idades
#Parametro: Dataframe
#Retorno: nenhum
def plotaIdades(meuDataframe):
    x = meuDataframe['dob.age']
    y = meuDataframe['dob.age'].value_counts
    plt.hist(x,100)
    plt.savefig('.\\Saida\\'+timestampArquivo+".png")

#verifica se o diretório de saída existe, caso não, cria
existe = os.path.exists(caminhoSaida)
if not existe:
    os.makedirs(caminhoSaida)

#acessa a API e monta o dataframe
dataframeOriginal = getData(600)

#formata os numeros de celular e de telefone fixo
DataframeTratada = transformaCelulares(dataframeOriginal,'cell')
DataframeTratada = transformaCelulares(dataframeOriginal,'phone')

#Grava em arquivo CSV
escreveResultado(DataframeTratada)
plotaIdades(DataframeTratada)

#Imprime os calculos de porcentagem
print(gravaEstatisticas(DataframeTratada))
    
