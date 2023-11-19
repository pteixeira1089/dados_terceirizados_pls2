"""Extrai um único conjunto de dados de todos os arquivos html de terceirizados salvos, agrupados por função"""
from pathlib import Path
from datetime import datetime, timedelta
from test_functions import nome_data_arquivo
import csv
import terceirizados_stj


# Constrói o caminho da pasta onde os html estão salvos
pasta_trabalho = Path.cwd()
pasta_trabalho = pasta_trabalho / "dados_html"

# Constrói uma lista de arquivos html fonte de dados
lista_arquivos = [arquivo for arquivo in pasta_trabalho.iterdir()]

# Constrói um dicionário de dados de arquivos com o respectivo resultado do teste de integridade nome/data do relatório
dic_arquivos_integridade_nome = {arquivo: nome_data_arquivo(arquivo, terceirizados_stj.FontesDados(arquivo)) for arquivo in lista_arquivos}
lista_arquivos_falhas_integridade_nome = [arquivo for arquivo in dic_arquivos_integridade_nome if dic_arquivos_integridade_nome[arquivo] == False]

# Constrói uma lista de objetos de fontes de dados
meta_dados_fontes = [terceirizados_stj.FontesDados(arquivo) for arquivo in lista_arquivos]

#Constrói um dicionário de dados com índices sendo o path do arquivo, e valores sendo a data do arquivo
dic_data_arquivo = {fonte.arquivo: fonte.data_relatorio for fonte in meta_dados_fontes}

# Constrói lista de datas de arquivos já salvos
lista_datas_salvas = [dic_data_arquivo[item] for item in dic_data_arquivo]

dic_datas_duplicadas = {path: dic_data_arquivo[path] for path in dic_data_arquivo if lista_datas_salvas.count(dic_data_arquivo[path]) > 1}

#Constrói lista de todas as datas a serem verificadas
start_date = datetime(year=2014, month=1, day=1)
end_date = datetime(year=2023, month=10, day=1)

lista_datas_verificar_arquivo = []

while start_date <= end_date:
    if start_date.day == 1:
        lista_datas_verificar_arquivo.append(start_date)
    start_date += timedelta(days=1)

lista_arquivos_ausentes = [data for data in lista_datas_verificar_arquivo if data not in lista_datas_salvas]


#Cria um csv a partir dos arquivos obtidos na lista (logging)
#Arquivos duplicados
with open('datas_duplicatas.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['data_do_arquivo', 'nome_do_arquivo'])
    for path in dic_datas_duplicadas:
        row = [dic_datas_duplicadas[path], path]
        writer.writerow(row)

with open('datas_ausentes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for data in lista_arquivos_ausentes:
        writer.writerow([data])

with open('falhas_integridade_nome_arquivo.csv', 'w', newline ='') as file:
    writer = csv.writer(file)
    for data in lista_arquivos_falhas_integridade_nome:
        writer.writerow([data])
