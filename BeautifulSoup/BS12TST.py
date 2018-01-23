# Looking for brotherssss


from bs4 import *

with open('arquivo03.html','r') as arquivo:
	soup = BeautifulSoup(arquivo, 'lxml')

# find_next_sibling, busca para baixo, irmãos
# find_previous_siblind, busca para cima, os irmãos

producers = soup.find(id='producers')

next_sibling = producers.find_next_sibling() # com "siblings" no final, ele imprime todas as ocorrências
print(next_sibling)

next_siblings = producers.find_next_siblings() # 
print(next_siblings)


producers = soup.find(id='quaternaryconsumers')
previous_sibling = producers.find_previous_sibling()
print(previous_sibling)



roducers = soup.find(id='quaternaryconsumers')
previous_siblings = producers.find_previous_siblings()
print(previous_siblings)
