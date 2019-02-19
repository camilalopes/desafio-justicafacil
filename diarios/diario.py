import requests
import hashlib
from bs4 import BeautifulSoup

URL_PDF = 'http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/diario.do?action=downloadDiario'
URL = 'http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/diario.do?action=buscarDiarios&page=diarioPageLastList.jsp&voDiarioSearch.tribunal=TSE&voDiarioSearch.calendario=false&voDiarioSearch.dataPubIni=01/02/2018&voDiarioSearch.dataPubFim=01/02/2018'


req = requests.get(URL)
soup = BeautifulSoup(req.content, 'html.parser')
links = soup.find_all('a')

#retorna a lista com o id dos pdfs a serem baixados
ids = []
for link in links:
    str = link['href']
    #para extrair o id do pdf da string, ele está entre ( e ,
    inicio_str_id = str.find('(')
    fim_str_id = str.find(',')
    #id do pdf
    id = str[inicio_str_id+1:fim_str_id]
    ids.append(id)

print(ids)

#id do PDF
#print(links[0]['href'][inicio_str_id+1:fim_str_id])

data = {"id":"86737",
        "tribunal":"TSE",
        "captchaValidacao":"ok"}
req = requests.post(URL_PDF, params = data)

#hash do pdf
print (hashlib.md5(req.content).hexdigest())
