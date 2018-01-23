from bs4 import *

with open('arquivo04.html','r') as arquivo:
	soup = BeautifulSoup(arquivo, 'lxml')
'''
primaryconsumers = soup.find_all(class_='primaryconsumerlist')
primaryconsumer = primaryconsumers[0]
print(primaryconsumer)'''

#parent_ul = primaryconsumer.find_parents('ul') # Procura o parent da ul

