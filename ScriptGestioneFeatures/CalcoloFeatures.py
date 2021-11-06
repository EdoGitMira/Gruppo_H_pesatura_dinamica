from math import *
from statistics import *


def calcolo_feature_statiche(nomeTxT,file):
    """in questo prendiamo il file txt lo spezziamo più volte in modo da leggere l'ultima colonna e calcolare la media e la
           deviazione standard, ritorniamo poi una tupla con i 3 elementi grammi,media,deviazione standard"""

    somma = 0
    conta = 0
    data = []
    grammi = nomeTxT.split('.')[0]

    if grammi == '607g':
        print()

    for (i, element) in enumerate(file):
        if i >= 5:
            element = element.decode('utf-8')
            row = element.split('\t')[1].split('\n')[0].split('E')
            numero = float(row[0].replace(',', '.'))
            esponente = int(row[1])

            actualData = round(numero * pow(10, esponente), 10)
            data.append(actualData)

    media = mean(data)
    std_dev = stdev(data)
    riga = (grammi,media,std_dev)

    return riga

