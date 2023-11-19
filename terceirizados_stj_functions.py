"""Funções utilizadas no script de extração de dados de terceirização"""
import csv
from pathlib import Path

def novo_csv(endereco_pasta: Path, nome_arquivo: str, colunas: list):
    #Adiciona extensão ao nome do arquivo fornecido
    nome_arquivo = nome_arquivo + '.csv'

    #Constrói o caminho onde o arquivo será criado
    caminho = endereco_pasta / nome_arquivo
    
    #Cria o arquivo
    with open(caminho, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(colunas)