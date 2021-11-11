from math import *
from statistics import *





def calcolo_feature_statiche( file, mass_name):
    """in questo prendiamo il file txt lo spezziamo più volte in modo da leggere l'ultima colonna e calcolare la media e la
           deviazione standard, ritorniamo poi una tupla con i 3 elementi grammi,media,deviazione standard"""
    std_deviations = []
    data = []
    for (i, element) in enumerate(file):
        if i > 5:
            element = element.decode('utf-8')
            row = element.split('\t')[1].split('\n')[0].split('E')

            number = float(row[0].replace(',', '.'))  # number without exponent
            exponent = int(row[1])  # exponent of number

            data.append(round(number * pow(10, exponent), 10))  # number float format and append data

    media = mean(data)
    std_dev = stdev(data)
    riga = (str(mass_name), str(media), str(std_dev))

    return riga
