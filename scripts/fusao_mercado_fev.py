import json 
import csv

# setando a pasta de arquivos do Load :
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# convertendo conteudo dos arquivos em variáveis : 
def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json

# convertendo conteudo dos arquivos em variáveis : 
def leitura_csv(path_csv):
    with open(path_csv, 'r') as file :
        spamreader = csv.reader(file, delimiter=',')
        dados_csv = []
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv

# função de leitura de dados : 
def leitura_dados(path,tipo_arquivo):
    
    dados = []
    
    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)
    elif tipo_arquivo == 'json':
        dados = leitura_json(path)

    return dados


# chama função de leitura de dados :
# print(leitura_dados(path_json,'json'))


