"""Funções de testes de integridade dos arquivos"""
#import datetime
from pathlib import Path
from terceirizados_stj import FontesDados


def nome_data_arquivo(caminho: Path, fonte: FontesDados):
    """Recebe o caminho do arquivo a ser testado e o respectivo objeto fonte a ele associado
    Retorna tupla contendo a data usada no nome do arquivo"""
    data_nome_arquivo = str(caminho).split('\\')[-1].split('.')[0]
    data_arquivo = fonte.data_relatorio.strftime("%Y-%m-%d")
    return data_nome_arquivo == data_arquivo



#Isola o bloco de testes
if __name__ == "__main__":

    # Constrói o caminho da pasta onde os html estão salvos
    pasta_trabalho = Path.cwd()
    pasta_trabalho = pasta_trabalho / "dados_html"

    # Constrói uma lista de arquivos html fonte de dados
    lista_arquivos = [arquivo for arquivo in pasta_trabalho.iterdir()]

    arquivo_teste = lista_arquivos[0]
    fonte_teste = FontesDados(arquivo_teste)

    saida_teste = nome_data_arquivo(arquivo_teste, fonte_teste)

    print(saida_teste)
