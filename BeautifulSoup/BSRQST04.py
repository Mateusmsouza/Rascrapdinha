import requests

busca = 'celular'
url = 'https://www.submarino.com.br/busca?conteudo={0}'.format(busca) #Pulo do gato
site = requests.get('https://www.submarino.com.br/')
cookie = site.cookies.get_dict() # Captura o cookie

request = requests.get(url, cookies=cookie)

with open('submarino.html','w') as arq:
	arq.write(request.text)
	arq.close()
