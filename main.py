# -*_ encoding: utf-8 -*-

import os
from scraping import scraping
from download import download
from dataProcessing import processing

def clear(): return os.system('clear')

url = "http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar"

pdfFileName = download(scraping(url))
csvFileName = processing(pdfFileName)
clear() 

print('URL: '+url)
print('Arquivo '+pdfFileName+' baixado.')
print('Tabelas extraidas e salvas em '+csvFileName+'.')