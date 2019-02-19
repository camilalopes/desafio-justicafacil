from selenium import webdriver
import time

DOWNLOAD_PATH = "C:\\Users\\Camila\\Downloads"

options = webdriver.ChromeOptions()
preferences = {"download.default_directory": DOWNLOAD_PATH, "directory_upgrade": True, "safebrowsing.enabled": True }
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(options=options)

driver.get("http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/diario.do?action=buscarDiarios&page=diarioPageLastList.jsp&voDiarioSearch.tribunal=TSE&voDiarioSearch.calendario=false&voDiarioSearch.dataPubIni=01/02/2018&voDiarioSearch.dataPubFim=01/02/2018")

injected_javascript = 'document.getElementById("id").value = 86737; document.getElementById("tribunal").value = "TSE"; document.getElementById("captchaValidacao").value = "ok"; document.getElementById("formDocumentoDownload").submit();'
