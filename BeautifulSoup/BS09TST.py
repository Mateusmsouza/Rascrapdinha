from bs4 import BeautifulSoup

with open('arquivo04.html','r') as arquivo:
	soup = BeautifulSoup(arquivo, 'lxml')

'''
tag = soup.find('li') # Procura por tag
print(tag)
'''
'''
tag = soup.find(string='plants')#Procura textos
print(tag) '''

'''
tag = soup.find(id='secondaryconsumers') # Procura por id dos elementos
print(tag)
'''
'''
tag = soup.find(attrs = {'class':'primaryconsumerlist'}) # Busca pelo css, note que é um dict
print(tag)
'''

'''
tag = soup.find('li', attrs={'class':'producerlist'}) # mais de um filtro
print(tag)
'''

'''
tag = soup.ul.li.find('li') #Aninhamento de tag + find
print(tag)
'''

def is_secondary_consumers(tag): #Função Filtro para interagir com find
	return tag.has_attr('id') and tag.get('id') == 'secondaryconsumers' # A cada tag, verifica se tem id, e após, se'essa id é igual a secondaryconsumers

secondary_consumer = soup.find(is_secondary_consumers) # find com a função
print(secondary_consumer.li.div.string)