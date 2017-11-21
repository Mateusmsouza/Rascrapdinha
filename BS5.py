'''
Baseado no Livro http://zempirians.com/ebooks/Ryan%20Mitchell-Web%20Scraping%20with%20Python_%20Collecting%20Data%20from%20the%20Modern%20Web-O%27Reilly%20Media%20(2015).pdf
Finding the originals shows from Netflix.com
'''

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def graburl(link):
    global page
    try:
        page = urlopen(link) # glabbing the html
    except HTTPError as error:
        print(error)
        print("Deu ruim")
        return None

    try:
        bsobj = BeautifulSoup(page, 'html.parser')
        return bsobj.findAll("div",{"class":"original-title"}) #finding our list
    except AttributeError as error:
        print(error)
        return None

Listaum = graburl('https://www.netflix.com/br/originals')

for filme in Listaum: # and here the final and the magic
    print(filme.get_text())
