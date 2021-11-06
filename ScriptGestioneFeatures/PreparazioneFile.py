import urllib
from os import *
# noinspection PyCompatibility
from pathlib import Path
# noinspection PyCompatibility
from urllib import request
import CalcoloFeatures


def lista_features_statico(url,path):

    lista = listdir(path)  # lista dei nomi dei file .txt

    data = []

    for nome_file in lista:
        url_github = url + '/' + nome_file  # attacco all'url il nome del file .txt
        file = urllib.request.urlopen(url_github)
        riga = CalcoloFeatures.calcolo_feature_statiche(nome_file, file)
        data.append(riga)

    return data

def read_names_url_txt(url):
    names = []
    for element in urllib.request.urlopen(url):
        names.append(element.decode('utf-8'))
    return names
