# Usando o request
import requests

url = 'https://www.youtube.com/results?'

payload = {'search_query':'Naruto'} 

site = requests.get(url, params=payload)

print(site.text)
print(site.url) # Trará o link
print(site.encoding) # Encode

with open('youtube.html','wb') as arquivo:
	arquivo.write(site.content)