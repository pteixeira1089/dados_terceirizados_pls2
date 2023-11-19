"""Define os objetos usados para a extração dos dados de terceirização
Para maiores detalhes dos critérios adotados, consulte o arquivo abaixo:
https://stjjus.sharepoint.com/:w:/s/AGSTeams/EZMHcEivmPBBmOO77XILE_MBP0CDsaaMwh-mZ8Q31XVhng?e=VRMwg4"""

import terceirizados_stj

#Critérios de busca de terceirizados de jardinagem
# Período: 06/03/2012 a 05/03/2015
jardinagem1 = terceirizados_stj.CriteriosExtracao(
    empresa= r'SANTA HELENA URBANIZAÇÃO E OBRAS LTDA.',
    data_inicio='2012-03-06',
    data_fim='2017-03-19'
)

#Critérios de busca de terceirizados de jardinagem
# Período: 02/09/2015 a 01/09/2020
jardinagem2 = terceirizados_stj.CriteriosExtracao(
    empresa= r'TERRA VIVA SERVICOS DE JARDINAGEM LTDA - ME',
    data_inicio='2017-03-20',
    data_fim='2020-09-14'
)

#Critérios de busca de terceirizados de jardinagem
# Período: 02/09/2020 a 01/09/2025
jardinagem3 = terceirizados_stj.CriteriosExtracao(
    empresa= r'UNISERVE COMERCIO E SERVICOS TERCEIRIZADOS LTDA',
    data_inicio='2020-09-15',
    data_fim='2025-09-01'
)

#Lista de objetos que pode ser utilizada no script principal ao extrair dados relativos a jardinagem
jardinagem = [jardinagem1, jardinagem2, jardinagem3]