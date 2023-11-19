from pathlib import Path
import terceirizados_stj as trc

#Constrói o caminho da pasta onde os html estão salvos
pasta_trabalho = Path.cwd()
pasta_trabalho = pasta_trabalho / "dados_html"

#Carrega arquivo teste para extração
lista_arquivos = [arquivo for arquivo in pasta_trabalho.iterdir()]
arquivo_teste = lista_arquivos[0]


#Carrega dados de terceirizados do html salvo
dados_terceirizados = trc.DataFrameTerceirizados(
   arquivo_teste, 0)

df_dados_terceirizados = dados_terceirizados.data_frame

# Obtém dados de terceirizados da empresa de jardinagem
num_coluna_filtro = 1
lista_valores_filtro = ["SANTA HELENA URBANIZAÇÃO E OBRAS LTDA."]

# Atualiza os atributos do objeto dados_terceirizados de acordo com os valores passados acima
dados_terceirizados.filtra_dataframe_original(
    num_coluna_filtro, lista_valores_filtro)


#Obtém dataframe filtrado
df_jardinagem = dados_terceirizados.data_frame_filtrado

# # Obtém os valores de terceirizados total e de limpeza
# terceirizados_total = dados_terceirizados.quantidade_linhas
# terceirizados_limpeza = dados_terceirizados.quantidade_linhas_filtrado

# # Carrega os dados do arquivo a ser atualizado
# endereco_arquivo = r'C:\Users\pteix\STJ- Superior Tribunal de Justiça\AGS Teams - Documentos\1. Drive H AGS\Assessoria\0 Dados\PLS\GRUPOEXEC\1. TEMAS\GE Rec Tecnol\04. Impressão\QtdTerceirizados.csv'
# arquivo = trc.Arquivo(endereco_arquivo)

# # Carrega datas já registradas no arquivo
# datas = arquivo.datas_arquivo

# # Carrega a data do html analisado
# data_html = dados_terceirizados.data_arquivo()

# # Verifica se a data do html analisado já está no arquivo a ser atualizado
# # Caso não esteja:
# # Constrói o valor de data em formato reduzido, para inserção no arquivo csv;
# # Adiciona um novo registro ao atributo data_frame do objeto arquivo; e
# # Exporta este data_frame como um csv para o endereço do arquivo
# if data_html not in datas.values:
#     data_reduzida = str(data_html).split()[0]
#     new_row = {'data': [data_reduzida], 'terceirizados': [
#         terceirizados_total], 'terceirizados_limpeza': [terceirizados_limpeza]}
#     arquivo.acrescenta_registro(new_row)
#     arquivo.exporta_arquivo()

