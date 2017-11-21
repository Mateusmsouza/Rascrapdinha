'''
Exemplo do Livro http://zempirians.com/ebooks/Ryan%20Mitchell-Web%20Scraping%20with%20Python_%20Collecting%20Data%20from%20the%20Modern%20Web-O%27Reilly%20Media%20(2015).pdf
'''
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as error: # Tratando o erro de servidor não achado.
    print(error)


else: 
    if html is None: # Verificado se o html não retornou None 
        print("URL troll")
    else: # Se tudo ok, continua a execução.
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        
        try: # Procura a tag h1
            h1 = bsObj.h1
        except AttributeError as erro:
            print("Tag não encontrada")
            print(erro)
        else:
            print(h1)
            print("Segue o baile")
