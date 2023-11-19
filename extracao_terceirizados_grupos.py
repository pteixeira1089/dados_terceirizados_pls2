"""Extrai um único conjunto de dados de todos os arquivos html de terceirizados salvos, agrupados por função"""
from pathlib import Path
import terceirizados_stj
import pandas as pd

# Constrói o caminho da pasta onde os html estão salvos
pasta_trabalho = Path.cwd()
pasta_trabalho = pasta_trabalho / "dados_html"

# Constrói uma lista de arquivos html fonte de dados
lista_arquivos = [arquivo for arquivo in pasta_trabalho.iterdir()]

# Constrói uma lista de dataframes agrupados por função a partir de cada arquivo da lista_arquivos
lista_df_agrupados = [terceirizados_stj.DataFrameTerceirizados(
    arquivo, 0).data_frame_agrupado for arquivo in lista_arquivos]

# Concatena todos os dataframes
df_agrupado = pd.concat(lista_df_agrupados)

#Exporta o dataframe agrupado
df_agrupado.to_csv('terceirizados_por_funcao.csv')
