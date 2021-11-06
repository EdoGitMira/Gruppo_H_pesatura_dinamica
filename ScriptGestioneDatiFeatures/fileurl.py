from pathlib import Path
from os import *
from urllib import request

def somma(a,b):
    return a+b

def readTxtUrl(url):
    path = Path(__file__).parent / "../dati/taratura"  # path relativa quindi torna indietro e poi va avanti nelle cartelle definite.
    lista = listdir(path)
    data = []
    for name in lista:
        urlc = url + name
        print('-' * 100)
        filedata = []
        for line in request.urlopen(urlc):
            filedata.append(line)
        data.append(filedata)
    return data