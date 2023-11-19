import terceirizados_stj as trc

# Carrega dados de terceirizados do html salvo
dados_terceirizados = trc.DataFrameTerceirizados(
    'terceirizados_2023_07_html_completo.html', 0)

# Obtém dados de terceirizados da limpeza
num_coluna_unidades_lotacao = 4
unidades_lotacao = ["Seção de Limpeza e Conservação",
                    "Coordenadoria de Conservação Predial", "Seção de Administração de Edifícios"]

num_coluna_atividades = 3
atividades = ["Jauzeiro", "Servente",
              "Supervisor", "Supervisor Geral de Serventes"]

# Atualiza os atributos do objeto dados_terceirizados de acordo com os valores passados acima
dados_terceirizados.filtra_dataframe_original(
    num_coluna_unidades_lotacao, unidades_lotacao)
dados_terceirizados.filtra_dataframe_filtrado(
    num_coluna_atividades, atividades)

# Obtém os valores de terceirizados total e de limpeza
terceirizados_total = dados_terceirizados.quantidade_linhas
terceirizados_limpeza = dados_terceirizados.quantidade_linhas_filtrado

# Carrega os dados do arquivo a ser atualizado
endereco_arquivo = r'C:\Users\pteix\STJ- Superior Tribunal de Justiça\AGS Teams - Documentos\1. Drive H AGS\Assessoria\0 Dados\PLS\GRUPOEXEC\1. TEMAS\GE Rec Tecnol\04. Impressão\QtdTerceirizados.csv'
arquivo = trc.Arquivo(endereco_arquivo)

# Carrega datas já registradas no arquivo
datas = arquivo.datas_arquivo

# Carrega a data do html analisado
data_html = dados_terceirizados.data_arquivo()

# Verifica se a data do html analisado já está no arquivo a ser atualizado
# Caso não esteja:
# Constrói o valor de data em formato reduzido, para inserção no arquivo csv;
# Adiciona um novo registro ao atributo data_frame do objeto arquivo; e
# Exporta este data_frame como um csv para o endereço do arquivo
if data_html not in datas.values:
    data_reduzida = str(data_html).split()[0]
    new_row = {'data': [data_reduzida], 'terceirizados': [
        terceirizados_total], 'terceirizados_limpeza': [terceirizados_limpeza]}
    arquivo.acrescenta_registro(new_row)
    arquivo.exporta_arquivo()

