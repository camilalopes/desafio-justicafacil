import requests
import hashlib
from bs4 import BeautifulSoup

URL = 'http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/'
URL_PDF = URL+'diario.do?action=downloadDiario'
URL_DATA = URL+'diario.do?action=buscarDiarios&page=diarioPageLastList.jsp&voDiarioSearch.tribunal=TSE&voDiarioSearch.calendario=false'

'''Retorna a lista com o id dos pdfs a serem baixados de acordo com a data'''
def lista_id_pdfs(data):
    param = {"voDiarioSearch.dataPubIni": data,
                "voDiarioSearch.dataPubFim": data}
    req = requests.get(URL_DATA, param)
    soup = BeautifulSoup(req.content, 'html.parser')
    links = soup.find_all('a')

    pdf_ids = []
    for link in links:
        str = link['href']
        #limite para extrair o id do pdf da string, ele está entre ( e ,
        inicio_str_id = str.find('(')
        fim_str_id = str.find(',')
        #id do pdf
        id = str[inicio_str_id+1:fim_str_id]
        pdf_ids.append(id)
    return pdf_ids

'''Retorna uma lista de hashes para uma lista de pdfs passada'''
def lista_hash_pdf(pdf_ids):
    lista_hash = []
    for pdf_id in pdf_ids:
        param = {"id": pdf_id,
                "tribunal":"TSE",
                "captchaValidacao":"ok"}
        req = requests.post(URL_PDF, params = param)
        #hash do pdf
        hash = hashlib.md5(req.content).hexdigest()
        lista_hash.append(hash)
    return lista_hash

'''Retorna uma lista de hashes para uma determinada data passada'''
def lista_hash(data):
    pdf_ids = lista_id_pdfs(data)
    lista_hashes = lista_hash_pdf(pdf_ids)
    return lista_hashes

def main():
    data = '01/02/2018'
    print(lista_hash(data))

if __name__ == "__main__":
	main()
