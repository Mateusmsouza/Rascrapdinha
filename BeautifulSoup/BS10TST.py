from bs4 import *

with open('arquivo03.html','r') as arq:
	soup = BeautifulSoup(arq, 'lxml')
'''
tag_list = soup.find_all('ul')
print(tag_list)
'''

'''
tag_list = soup.find_all(['ul','div']) # passando uma lista para o find_all
print(tag_list)
'''

#tag_list = soup.find_all('ul', limit=2) # Limitando até duas ocorrências

#tag_list = soup.find_all(string='rabbit') # Buscando pelo texto rabbit

#tag_list = soup.find_all(string=True) # Buscando todas as strings 

#tag_list=soup.find_all(string=['rabbit','bear']) # Passando uma lista para procurar

#tag_list = soup.find_all(class_=['producerlist','anotherclass']) # Lista de classes

#tag_list = soup.find_all('div', class_='name') # Passando para a procura a div e uma classe