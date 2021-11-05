import urllib.request
from statistics import *
from math import *
from pathlib import Path
from os import *
from urllib import request


url = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati/taratura/'


path = Path(__file__).parent / "../dati/taratura"  #path relativa quindi torna indietro e poi va avanti nelle cartelle definite.
lista = listdir(path)

for file in lista:
    data= url + file
    print('-'*100)
    for line in urllib.request.urlopen(data):
        print()

somma = 0
conta = 0
data = []

"""in questo prendiamo il file txt lo spezziamo più volte in modo da leggere l'ultima colonna e calcolare la media e la
deviazione standard"""


for (i,element) in enumerate(file.readlines()) :
    if i > 5:
        row = element.split('\t')[1].split('\n')[0].split('E')
        numero = float(row[0].replace(',', '.'))
        esponente = int(row[1])
        #print(data[0])
        actualData = round(numero * pow(10, esponente), 10)
        data.append(actualData)

media = mean(data)
std_dev = stdev(data)

print(f'media {media} \nsdt_dev = {std_dev}')



""" dobbiamo fare in modo di creare un txt con 3 colonne peso bilancia, media, e dev std"""

