#Material baseado nas aulas do curso de WebScraping da Udemy
from bs4 import BeautifulSoup

with open('arquivo02.html','r') as arquivo:
	soup = BeautifulSoup(arquivo,'lxml')

print(soup.title)
print(soup.a)
print(soup.td.attrs)
print(soup.td['class'])
print(soup.td['class'][0]) # Retorna o conteúdo da class, mt util sz
