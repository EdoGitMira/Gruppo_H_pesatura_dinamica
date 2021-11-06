from pathlib import Path
from os import *
from urllib import request

def somma(a,b):
    return a+b

def readTxtUrl(url,urlnamemass):
    ''' funzione per la lettura di file .TXT da file .url di github in con link RAW'''

    path = Path(
        __file__).parent / "../dati/taratura"  # path relativa quindi torna indietro e poi va avanti nelle cartelle definite.
    lista = listdir(path)
    data = []

    #listaname  = []
    #for line in request.urlopen(urlnamemass):
    #    listaname.append(line)

    #for name in listaname:
    for name in lista:
        urlc = url + name
        print('-' * 100)
        filedata = []
        for line in request.urlopen(urlc):
            filedata.append(line)
        data.append(filedata)
    return data