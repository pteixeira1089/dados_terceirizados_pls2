"""Arquivo utilizado para fins de testes de blocos de código"""
import terceirizados_stj
from datetime import datetime
from pathlib import Path
from terceirizados_stj_functions import novo_csv

#Constrói o caminho da pasta onde os html estão salvos
pasta_trabalho = Path.cwd()
pasta_trabalho = pasta_trabalho / "dados_html"

#Constrói uma lista de arquivos html fonte de dados
lista_arquivos = [item for item in pasta_trabalho.iterdir()]

#Seleciona um arquivo para teste
arquivo_teste = lista_arquivos[0]

#Constrói um objeto do tipo DataFrameTerceirizados com o arquivo teste
df_terceirizados = terceirizados_stj.DataFrameTerceirizados(arquivo_teste, 0)

print('hello!')

print(df_terceirizados.data_frame_agrupado)
print(type(df_terceirizados.data_frame_agrupado))

print('hello2')




# #Cria um novo arquivo csv para receber a extração em massa de todos os dados de terceirização
# caminho = Path.cwd()
# nome_arquivo = 'terceirizados_historico_agrupado'
# novo_csv(caminho, nome_arquivo=nome_arquivo)



# #Constrói o caminho da pasta onde os html estão salvos
# pasta_trabalho = Path.cwd()
# pasta_trabalho = pasta_trabalho / "dados_html"

# #Constrói uma lista de arquivos html fonte de dados
# lista_arquivos = [item for item in pasta_trabalho.iterdir()]

# #Seleciona um arquivo para teste
# arquivo_teste = lista_arquivos[0]

# #Constrói um objeto do tipo
# df_terceirizados = terceirizados_stj.DataFrameTerceirizados(arquivo_teste, 0)

# #Filtra dataframe
# df_terceirizados.filtra_dataframe_original(3, texto='Secr')

# print('Hello!')