'''
Consultando a variação da Ibovespa
'''
import requests
from bs4 import BeautifulSoup

def Procura(self): # Função pra retornar o valor que ta largado no meio do código da página
    a = self.find(',')
    return self[a-1:a+3]

HTML = requests.get('http://www.infomoney.com.br/ibovespa')
HTML = HTML.content
HTML = BeautifulSoup(HTML,'html.parser')

SpanPorcentagem = HTML.find('span', attrs={'class':'negativo'}) # Achando a agulha no palheiro


sinal = str(SpanPorcentagem.sub.contents)
value = str(SpanPorcentagem.strong)
value = Procura(value)
print("Variação da Ibovespa:",sinal[2:3]+value+'%')
