import requests
import hashlib
from bs4 import BeautifulSoup

URL = 'http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/'
URL_PDF = URL+'diario.do?action=downloadDiario'
URL_DATA = URL+'diario.do?action=buscarDiarios&page=diarioPageLastList.jsp&voDiarioSearch.tribunal=TSE&voDiarioSearch.calendario=false'

param = {"voDiarioSearch.dataPubIni":"14/06/2017",
            "voDiarioSearch.dataPubFim":"14/06/2017"}
req = requests.get(URL_DATA, param)

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

param = {"id":"86737",
        "tribunal":"TSE",
        "captchaValidacao":"ok"}
req = requests.post(URL_PDF, params = param)

#hash do pdf
print (hashlib.md5(req.content).hexdigest())
