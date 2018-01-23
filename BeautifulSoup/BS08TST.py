from bs4 import BeautifulSoup
from bs4.element import Tag

with open('arquivo03.html','r') as arquivo:
	soup = BeautifulSoup(arquivo, 'lxml')


#print(soup.div.next_element.next_element)
#print(soup.li.previous_element.previous_element)

'''
for elemento in soup.ul.next_elements:
	if isinstance(elemento, Tag):
		print(elemento)
		'''

for elemento in soup.li.previous_elements:
	print(repr(elemento))