import requests
# Simulando um agente browser
# Tradutor Português <-> Inglês

url = "https://www.linguee.com.br/portugues-ingles/search?"

payload = {'source':'auto',
			'query':'Ball'} # Aqui é onde fica a palavra a ser traduzida

header={'Origin':'https://www.linguee.com.br',
		'Referer':'https://fonts.googleapis.com/css?family=PT+Sans:400,700&subset=latin,cyrillic,latin-ext,cyrillic-ext,vietnamese,greek-ext,greek',
		'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
		}

response = requests.get(url, params=payload, headers=header)

with open('linguee.html','w', encoding='utf-8') as arquivo:
		arquivo.write(response.text)
		arquivo.close()

print(response.request.headers)