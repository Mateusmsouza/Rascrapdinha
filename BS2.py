'''
Baixando sites em .html automáticamente
'''
import requests
from bs4 import BeautifulSoup

#Abrindo o arquivo html
HTML = open('index.html', 'w')

# Fazendo o get e tratando a página com BeautifulSoup
pagina = requests.get('https://www.uol.com.br/')
pagina = BeautifulSoup(pagina.content, 'html.parser')

# Escrevendo o código no arquivo HTML e fechando ele
HTML.write(str(BeautifulSoup(pagina.prettify(), "html.parser" )))
HTML.close()
