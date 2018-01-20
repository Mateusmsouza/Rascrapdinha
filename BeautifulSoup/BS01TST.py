#Material baseado nas aulas do curso de WebScraping da Udemy
import requests
from bs4 import BeautifulSoup
'''
def bs(self):
	inst = BeautifulSoup(self.text, 'lxml')
	return inst

r = requests.get('www.google.com')
bxml = bs(r)
'''
with open('arquivo.html','r') as f:
	soup = BeautifulSoup(f.read(), 'html5lib')
print(soup) 
