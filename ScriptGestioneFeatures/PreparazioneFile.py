import urllib
from os import *
# noinspection PyCompatibility
from pathlib import Path
# noinspection PyCompatibility
from urllib import request
import CalcoloFeatures


def prendo_file_url_statico():
    url = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati/taratura/'

    path = Path(__file__).parent / "../dati/taratura"  # path relativa quindi torna indietro e poi va avanti nelle cartelle definite.
    lista = listdir(path)  # lista dei nomi dei file .txt

    data = []

    for nome_file in lista:
        url_github = url + '/' + nome_file  # attacco all'url il nome del file .txt
        file = urllib.request.urlopen(url_github)
        riga = CalcoloFeatures.calcolo_feature_statiche(lista[0], file)
        data.append(riga)

    return data

def scrittura_txt(nome,directory,intestazione):

    return None






