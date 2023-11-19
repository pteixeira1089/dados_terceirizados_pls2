# Classes do script de modelagem e exportação de dados de terceirizados
# A exportação é feita a partir de uma página html retirada do site do STJ

import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import numpy as np


class DataFrameTerceirizados:
    """Data frame contendo os dados de terceirizados de uma dada página html retirada da intranet"""

    def __init__(self, html_address: str, df_position: int):
        self.html_address = html_address
        self.df_position = df_position
        self.data_frame = pd.read_html(
            html_address, encoding='utf-8')[df_position].iloc[1:, :]
        self.quantidade_linhas = len(self.data_frame.index)
        self.data_frame_filtrado = None
        self.quantidade_linhas_filtrado = None
        self.soup = BeautifulSoup(open(html_address), 'lxml')
        self.data_relatorio = self.data_arquivo()
        self.data_frame_agrupado = self.agrupa_por_funcao()

    def filtra_dataframe_original(self, nome_col: 'str', lista_valores: 'list' = None, texto: 'str' = None):
        """Filtra o dataframe original e atribui o valor resultante ao dataframe_filtrado"""
        
        #Error Handling
        if lista_valores is not None and texto is not None:
            raise ValueError('Você deve especificar uma lista de valores exatos ou um texto de busca, mas não ambos')
        if lista_valores is None and texto is None:
            raise ValueError('Você deve dar uma lista de valores exatos ou um texto para busca aproximada')
        
        #Caso em que o usuário fornece uma lista de valores exatos para pesquisa
        if lista_valores is not None:
            self.data_frame_filtrado = self.data_frame.loc[self.data_frame[nome_col].isin(
                lista_valores)]
            self.quantidade_linhas_filtrado = len(self.data_frame_filtrado.index)
            pass

        #Caso em que o usuário fornece um texto para pesquisa
        else:
            self.data_frame_filtrado = self.data_frame.loc[self.data_frame[nome_col].str.contains(texto)]
            self.quantidade_linhas_filtrado = len(self.data_frame_filtrado.index)

    def filtra_dataframe_filtrado(self, nome_col: 'str', lista_valores: 'list' = None, texto: str = None):
        """Filtra o dataframe filtrado e atribui o valor resultante ao atributo data_frame_filtrado"""
        
        #Error Handling
        if lista_valores is not None and texto is not None:
            raise ValueError('Você deve especificar uma lista de valores exatos ou um texto de busca, mas não ambos')
        if lista_valores is None and texto is None:
            raise ValueError('Você deve dar uma lista de valores exatos ou um texto para busca aproximada')
        
        #Caso em que o usuário fornece uma lista de valores exatos para pesquisa
        if lista_valores is not None:
            self.data_frame_filtrado = self.data_frame_filtrado.loc[self.data_frame_filtrado[nome_col].isin(
                lista_valores)]
            self.quantidade_linhas_filtrado = len(self.data_frame_filtrado.index)
            pass

        #Caso em que o usuário fornece um texto para pesquisa
        else:
            self.data_frame_filtrado = self.data_frame_filtrado.loc[self.data_frame_filtrado[nome_col].str.contains(texto)]
            self.quantidade_linhas_filtrado = len(self.data_frame_filtrado.index)
            pass


    def data_arquivo(self):
        """Extrai a informação de data referente à atualização"""
        tag_html = self.soup.find_all('div')[1]
        texto = tag_html.find(text=True).strip()
        raw_date = texto.split(" ")[-1]
        month_date = raw_date.split("/")[1]
        year_date = raw_date.split("/")[2]
        return datetime.strptime('{}-{}-01'.format(year_date, month_date), r'%Y-%m-%d')
    
    def agrupa_por_funcao(self):
        """Cria um dataframe agrupado por função"""
        
        #Cria uma lista de colunas que devem ser excluídas [somente a coluna 3 deve permanecer]
        #lista_exclusoes = [col for col in self.data_frame.columns if str(col) != '3']
        
        #Dropa a coluna 0, que contém o nome dos terceirizados
        #return self.data_frame.drop(columns=lista_exclusoes, axis=1)
        
        #Agrupa dados por função com a respectiva contagem de registros
        group_funcao = self.data_frame.groupby(3)
        group_funcao = group_funcao.agg({3: ['count']})
        group_funcao = group_funcao.reset_index()

        #Define nome padrão de colunas
        cols = ['funcao', 'qtd_terceirizados']
        group_funcao.columns = cols

        #Insere a data como uma coluna
        group_funcao['data'] = self.data_relatorio

        return group_funcao


class FontesDados:
    """Subclasse de DataFrameTerceirizados que contém apenas metadados dos arquivos fonte"""
    def __init__(self, html_address: str):
        self.arquivo = html_address
        self.soup = BeautifulSoup(open(html_address), 'lxml')
        self.data_relatorio = self.data_arquivo()
    
    def data_arquivo(self):
        """Extrai a informação de data referente à atualização"""
        tag_html = self.soup.find_all('div')[1]
        texto = tag_html.find(text=True).strip()
        raw_date = texto.split(" ")[-1]
        month_date = raw_date.split("/")[1]
        year_date = raw_date.split("/")[2]
        return datetime.strptime('{}-{}-01'.format(year_date, month_date), r'%Y-%m-%d')


class Arquivo:

    def __init__(self, file_address):
        self.endereco = file_address
        self.data_frame = pd.read_csv(file_address)
        self.datas_arquivo = pd.to_datetime(self.data_frame['data'])
        self.ultima_atualizacao = pd.to_datetime(self.data_frame['data']).max()
        self.ultima_atualizacao_mes = self.ultima_atualizacao.month
        self.ultima_atualizacao_ano = self.ultima_atualizacao.year

    def acrescenta_registro(self, new_row):
        """Acrescenta um novo registro ao atributo data_frame"""
        self.data_frame = pd.concat(
            [self.data_frame, pd.DataFrame(new_row)], ignore_index=True)

    def exporta_arquivo(self):
        """Exporta o data_frame para o endereço do objeto no formato csv"""
        self.data_frame.to_csv(self.endereco, index=False)

    def reseta_data_frame(self, lista_colunas: 'list'):
        """Reinicia o dataframe que será exportado para o arquivo csv,
        criando um novo dataframe com as colunas passadas no argumento lista_colunas"""
        self.data_frame = pd.DataFrame(columns=lista_colunas)


class CriteriosExtracao:
    """Classe que define os critérios de extração a serem utilizados para um 
    determinado grupo de terceirizados.
    Por exemplo: a classe que de critérios de extração de dados de terceirizados da jardinagem 
    contém dados da empresa fornecedora desses serviços e o período em que ela atuou"""

    def __init__(self, empresa: 'str', data_inicio: 'str', data_fim: str):
        self.empresa = empresa
        self.data_inicio = data_inicio
        self.data_fim = data_fim



