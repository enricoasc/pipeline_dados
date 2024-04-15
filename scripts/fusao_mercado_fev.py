import json 
import csv

# Convertendo conteudo dos arquivos em variáveis : 
def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json

# Convertendo conteudo dos arquivos em variáveis : 
def leitura_csv(path_csv):
    with open(path_csv, 'r') as file :
        spamreader = csv.DictReader(file,delimiter=',') 
        dados_csv = []
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv

# Função de leitura de dados : 
def leitura_dados(path,tipo_arquivo):
    dados = []
    
    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)
    elif tipo_arquivo == 'json':
        dados = leitura_json(path)

    return dados

# Extrai as chaves dos dados
def get_columns(dados):
    chaves = []
    chaves = list(dados[0].keys())
    return chaves

# Altera o nome das colunas
def rename_columns(dados,key_mapping):
    new_dados = []

    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados.append(dict_temp)
    
    return new_dados

# Combina listas de dados
def combina_listas(dadosA,dadosB):
    combined_list = []
    if(len(dadosA[0].keys()) > len(dadosB[0].keys()) ):
        combined_list.extend(dadosA)
        combined_list.extend(dadosB)
    else:
        combined_list.extend(dadosB)
        combined_list.extend(dadosA)

    return combined_list

# Trata colunas valores de colunas indisponíveis
def transformando_dados_tabela(dados, nome_colunas):
    dados_combinados_tabela = [nome_colunas]

    for row in dados:
        linha = []
        for coluna in nome_colunas:
            linha.append(row.get(coluna, 'indisponivel'))
        dados_combinados_tabela.append(linha)
    return dados_combinados_tabela

# Salva no destino os dados combinados e tratados
def salvando_dados_combinados(dados,path_final):
    with open(path_final, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados) ##  writerows - funciona com uma Lista de Listas
        

#######################################################
# Setando a pasta de arquivos do Load :
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# ---------------------------------------
# ..::: Extração - Iniciando leitura :
dados_csv = leitura_dados(path_csv,'csv')
dados_json = leitura_dados(path_json,'json')

nome_colunas_json = get_columns(dados_json)
nome_colunas_csv = get_columns(dados_csv)

print(f'Nome colunas json:{nome_colunas_json}')
print(f'Nome colunas csv:{nome_colunas_csv}')

# ---------------------------------------
# ..::: Transformação dos dados :
# - Padroniza as colunas
key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto' : 'Categoria do Produto',
               'Valor em Reais (R$)' : 'Preço do Produto (R$)',
               'Quantidade em Estoque' : 'Quantidade em Estoque',
               'Nome da Loja' : 'Filial',
               'Data da Venda' : 'Data da Venda' }

dados_csv = rename_columns(dados_csv,key_mapping)
nome_colunas_csv = get_columns(dados_csv)

print(f'Rename colunas csv:{nome_colunas_csv}')

# - Combina as duas listas
dados_combinados = combina_listas(dados_csv,dados_json)
nome_colunas_combinados = get_columns(dados_combinados)

print(f'Soma das duas listas : {len(dados_csv)+len(dados_json)}')
print(f'Total da lista combinada :{len(dados_combinados)}')

# - Transforma em tabela ( lista de Listas ) 
dados_combinados = transformando_dados_tabela(dados_combinados,nome_colunas_combinados)

# ---------------------------------------
# ..::: Salvando os Dados :

path_dados_combinados = 'data_processed/dados_combinados.csv'
salvando_dados_combinados(dados_combinados,path_dados_combinados)

print(f':.. Dados finalizados com sucesso ! ..: {path_dados_combinados}')


