import json 
import csv
class Dados:

    def __init__(self, path, tipos_dados):
        self.__path = path
        self.__tipo_dados = tipos_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()
        self.qtd_linhas = self.size_dados()


    # Convertendo conteudo dos arquivos em variáveis : 
    def __leitura_json(self):
        dados_json = []
        with open(self.__path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    # Convertendo conteudo dos arquivos em variáveis : 
    def __leitura_csv(self):
        with open(self.__path, 'r') as file :
            spamreader = csv.DictReader(file,delimiter=',') 
            dados_csv = []
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    # Função de leitura de dados : 
    def leitura_dados(self):
        dados = []

        if self.__tipo_dados == 'csv':
            dados = self.__leitura_csv()
        elif self.__tipo_dados == 'json':
            dados = self.__leitura_json()
        elif self.__tipo_dados == 'list':
            dados = self.__path
            self.__path = 'Lista em memoria'

        return dados

    # Extrai as chaves dos dados
    def get_columns(self):
        chaves = []
        chaves = list(self.dados[0].keys())
        return chaves

    # Altera o nome das colunas
    def rename_columns(self,key_mapping):
        new_dados = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)

        self.dados = new_dados
        self.nome_colunas = self.get_columns()
    
    # Contagem de dados
    def size_dados(self):
        return len(self.dados)
        
    # Combina listas de dados
    def combina_listas(dadosA,dadosB):
        combined_list = []
        if(len(dadosA.dados[0].keys()) > len(dadosB.dados[0].keys()) ):
            combined_list.extend(dadosA.dados)
            combined_list.extend(dadosB.dados)
        else:
            combined_list.extend(dadosB.dados)
            combined_list.extend(dadosA.dados)

        return Dados(combined_list,'list') 
    
    # Trata colunas valores de colunas indisponíveis
    def __transformando_dados_tabela(self):
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'indisponivel'))
            dados_combinados_tabela.append(linha)

        return dados_combinados_tabela

    # Salva no destino os dados combinados e tratados
    def salvando_dados_combinados(self,path_final):
        dados_combinados_tabela = self.__transformando_dados_tabela()

        with open(path_final, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela) ##  writerows - funciona com uma Lista de Listas
            