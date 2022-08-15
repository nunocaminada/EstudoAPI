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
    #le da API e coloca na codificação UTF-8
    meuDataframe = pd.read_csv(url, encoding='utf-8')
    return meuDataframe

#Objetivo: Escrever arquivo com dados da API Randomuser
#Parametro: Pandas dataframe
#Retorno: nenhum
def escreveResultado(meuDataframe):
    #monta um timestamp para dar nome ao arquivo
    timestampArquivo = time.strftime("%Y%m%d-%H%M%S")
    #grava um arquivo diferente a cada execução
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

#Objetivo: Imprimir percentual de pessoas por pais e por genero
#Parametro: Dataframe
#Retorno: nenhum
def calculaPorcentagem(meuDataframe):
    #calcula as porcentagens e formata a saída
    porcentagemPaises = ((meuDataframe['location.country'].value_counts()/meuDataframe['location.country'].count())*100).map('{:,.2f}%'.format)
    porcentagemGeneros = ((meuDataframe['gender'].value_counts()/meuDataframe['gender'].count())*100).map('{:,.2f}%'.format)
    #imprime os resultados
    print("Distribuicao percentual por pais")
    print(porcentagemPaises)
    print("\nDistribuicao percentual por genero")
    print(porcentagemGeneros)


#acessa a API e monta o dataframe
dataframeOriginal = getData(600)
#formata os numeros de celular
cellLimpos = transformaCelulares(dataframeOriginal)

#Grava em arquivo CSV
escreveResultado(cellLimpos)

#Imprime os calculos de porcentagem
print(calculaPorcentagem(cellLimpos))
    
