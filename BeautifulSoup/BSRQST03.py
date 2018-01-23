import requests

url = 'http://google.com/404'

request = requests.get(url)
print(request.status_code) # status de mensagem da resposta do http do server

if request.status_code == requests.codes.ok: # Igual a colocar == '200' !VALIDACODIGO!
	print('Keep going!')

print(request.headers) # Exibe o cabeçalho 
print(request.headers['Set-Cookie']) # Capturando o cookie usando o cabeçalho
print(request.request.headers) # Exibe o cabeçalho enviado para o site do google
