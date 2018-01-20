#Material baseado nas aulas do curso de WebScraping da Udemy
from bs4 import BeautifulSoup

with open('arquivo.html','r') as arquivo:
	soup = BeautifulSoup(arquivo, 'html.parser')

print(soup.p['class']) #Mostra o atributo class da tag p

print(soup.p.attrs) #mostra os atributos da tag p

print(soup.a['href']) #Mostra o link da tag href

# Usando o get

print(soup.a.get('href')) # It works!
