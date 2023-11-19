import terceirizados_stj as trc
from configuracoes_terceirizados import jardinagem
from datetime import datetime

# Carrega dados de terceirizados do html salvo
dados_terceirizados = trc.DataFrameTerceirizados(
    'terceirizados_2023_07_html_completo.html', 0)

#Obtém a data do relatório analisado
data_relatorio = dados_terceirizados.data_relatorio

# Percorre a lista de parâmetros para busca de terceirizados da jardinagem
# Identifica qual item da lista de parâmetros contém a data do arquivo analisado
for i, parametro in enumerate(jardinagem):
    data_inicio = datetime.strptime(parametro.data_inicio, r'%Y-%m-%d')
    data_fim = datetime.strptime(parametro.data_fim, r'%Y-%m-%d')
    
    if (data_relatorio >= data_inicio) and (data_relatorio <= data_fim):
        parametro_jardinagem = parametro
        break

#Cria uma lista contendo a empresa alvo da contagem
lista_empresa = [parametro.empresa]

# Atualiza os atributos do objeto dados_terceirizados de acordo com a empresa que contém os terceirizados alvo da contagem
# O filtro é aplicado à coluna 1, que contém o nome da empresa contratada
dados_terceirizados.filtra_dataframe_original(
    1, lista_valores=lista_empresa)

# Obtém os valores de terceirizados total e de jardinagem
terceirizados_total = dados_terceirizados.quantidade_linhas
terceirizados_filtro = dados_terceirizados.quantidade_linhas_filtrado

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

