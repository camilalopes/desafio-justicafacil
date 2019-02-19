import requests
import hashlib

URL = 'http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/diario.do?action=downloadDiario'
data = {"id":"86737",
        "tribunal":"TSE",
        "captchaValidacao":"ok"}
req = requests.post(URL, params = data)

#hash do pdf
print (hashlib.md5(req.content).hexdigest())


arq.close()
