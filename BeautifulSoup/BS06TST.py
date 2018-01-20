#Material baseado nas aulas do curso de WebScraping da Udemy
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

with open('arquivo02.html','r') as arquivo:
	soup = BeautifulSoup(arquivo, 'lxml')
'''
print(soup.table.contents[1]) # Isso gera uma lista, a tag será acessada pelo 1 pois o 0 da lista é um \n
print(soup.table.contents[1].span)
print(soup.table.contents[1].span.string)
print(soup.table.contents[3].td)

for child in soup.table.contents: #fazendo a magica de percorrer listas.
	if child.name == 'tr':
		print child


for child in soup.footer.children:
	print(child) # Dá pra colocar um .get('href'), chique show


print(len(list(soup.children))) #Acessa os filhos diretos
print(len(list(soup.descendants)) # Acessa as tags filhos indiretos tbm assim
'''

'''
for tag in soup.descendants:
	if isinstance(tag, NavigableString): # Verifica se é uma string
		print(tag) # Na vdd é uma string msm, por isso n tem .name

	else:
		print(tag.name)
'''
for tag in soup.descendants: 
	if isinstance(tag, Tag): # Verifica se é uma tag
		print(tag) 


for string in soup.aside.strings:
	print(repr(string)) # o repr gera representações para que o interpretador leia

for string in soup.aside.stripped_strings:
	print(repr(string)) # Printa sem o '\n', que seria trazido se fosse comparado apenas strings ao invés de stripped_strings
