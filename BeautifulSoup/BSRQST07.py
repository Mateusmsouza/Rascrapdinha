# Definindo time out
import requests

request = requests.get('www.google.com', timeout=0.03) # Setando 0.03 pra timeout (dá pra setar tempo de leitura usando timeout=(x,y))

print(request.url)

# Tratamento de exceções

try:
	requests.get('www.blabalbla.com')
except requests.exceptions.ConnectionError as error:
	print(str(error))
except requests.exceptions.HTTPError as error:
	print(str(error))
except requests.exceptions.Timeout as error:
	print(str(error))
except requests.exceptions.TooManyRedirects as error:
	print(str(error))
except requests.exceptions.RequestException as error:
	print(str(error))

