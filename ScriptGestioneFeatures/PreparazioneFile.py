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


def scrittura_txt(dati,directory = '',intestazione = '',nome = ''):

    percorso_completo = directory+nome

    file = open(percorso_completo,'w')
    file.write(intestazione)
    file.write('\n')

    for riga in dati:
        for elemento in riga:
            file.write(elemento)
            file.write('\t')
        file.write('\n')
    file.close()

    return None






