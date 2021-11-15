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


def sort_multiple_means(masses,means,std_dev):
    '''questo metodo riceve in ingresso i tre vettori già separati di peso, media e std_dev
    crea poi un unica lista con i tre elementi assieme e la ordina in ordine crescente di peso
    e poi la ritorna'''
    lista = [[masses[i],means[i],std_dev[i]] for i in range(len(masses))]
    lista.sort()
    return lista

def mean_of_means(lista):
    '''questo metodo riceve in ingresso la lista ordinara in ordine di peso crescente e calcola la media delle medie
    dei valori presenti, e la media delle std_dev, ritorna una lista più corta che contiene solo il numero effettivo di pesi
    non ripetuti, con rispettiva media e stddev'''

    num_pesate = 10
    list_mass = []
    list_mean = []

    lista_m_of_m = []
    i = 1

    precedente = lista[0][0]
    attuale = lista[0][0]

    for row in lista:

        attuale = row[0]
        if attuale > (precedente + 0.2):
            riga = [str(round(mean(list_mass), 2)), str(mean(list_mean)), str(stdev(list_mean))]
            lista_m_of_m.append(riga)
            list_mass.clear()
            list_mean.clear()
            precedente = attuale

        list_mass.append(attuale)
        list_mean.append(row[1])

    # manca la massa out of range di 1507

    return lista_m_of_m


