import requests

# Método POST

url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'

payload = {'relaxation':'12322430',
			'tipoCEP':'ALL',
			'semelhante':'N'}

response = requests.post(url, data=payload)


with open('correios.html','w') as arquivo:
	arquivo.write(response.text)