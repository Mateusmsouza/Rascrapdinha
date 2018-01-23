from bs4 import * 

with open('arquivo03.html','r') as arquivo:
	soup = BeautifulSoup(arquivo, 'lxml')

# Métodos
# find_next
# find_all_next
# find_previous
# find_all_previous
'''
producers = soup.find(id='producers') 
tag_next = producers.find_next() # Retorna o próximo, não depende de hierarquia
print(tag_next)'''
'''
producers = soup.find(id='producers') 
tag_next = producers.find_all_next() # Retorna todos os proximos, não depende de hierarquia
print(tag_next)'''
'''
producers = soup.find(id='quaternaryconsumers') 
tag_previous = producers.find_previous() # Retorna os anteriores a tag de id quartenaryconsumers
print(tag_previous)''' 

producers = soup.find(id='quaternaryconsumers') 
tag_previous = producers.find_all_previous() # Retorna todos os antecessores a tag de id quartenaryconsumers
print(tag_previous) 