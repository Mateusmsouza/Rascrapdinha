#Material baseado nas aulas do curso de WebScraping da Udemy
from bs4 import BeautifulSoup

with open('arquivo.html','r') as arquivo:
	soup = BeautifulSoup(arquivo, 'html5lib')

#print(soup.prettify()) # Exibe formatado
#print(soup.get_text()) # Retorna texto, nesse caso, de todas as tags

#print(soup.p.get_text()) # Retorna o texto da tag p

#print(soup.p.string # Imprime o texto APENAS da tag atual

print(soup.p.b.string) # Imprimindo na marra bino
