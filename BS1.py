html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
Sopinha = BeautifulSoup(html, 'html.parser')
print(Sopinha.prettify()) # Mostra a variável identada
print("-----------------------------------")
print(Sopinha.title.name) # Mostra o conteudo de <title>
print("-----------------------------------")
print(Sopinha.body) # Busca e exibe a tag body e seu conteúdo
print("-----------------------------------")
print(Sopinha.p['class']) # Exibe a class atribuída a primeir incidência de "p" com class
print("-----------------------------------")
print(Sopinha.a) # Exibe a primeira incidência da tag 'a'
print("-----------------------------------")
print(Sopinha.find_all('a')) # Exibe todas as incidências da tag ('<a>'), separando por virgula
print("-----------------------------------")
print(Sopinha.find(id="link2")) # Exibe a incidência que contém exatamente 'link2' em Id, *caso seja apenas link, não retornará a incidência link2*
print("-----------------------------------")
