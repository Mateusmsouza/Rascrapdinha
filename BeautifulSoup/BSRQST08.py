import requests

urlbase = 'http://compras.dados.gov.br'
cnpj = '07689002000189'
url = '{0}/contratos/v1/contratos.json?cnpj_contratada={1}'.format(urlbase, cnpj)

request = requests.get(url)
print(request.json())

