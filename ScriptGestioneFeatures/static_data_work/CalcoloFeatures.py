from random import *
from math import *
from statistics import *
from matplotlib import pyplot as plt



def calcolo_feature_statiche(file, mass_name = 0):
    """in questo prendiamo il file txt lo spezziamo più volte in modo da leggere l'ultima colonna e calcolare la media e la
           deviazione standard, ritorniamo poi una tupla con i 3 elementi grammi,media,deviazione standard, in più ritorna pure
           il 2 vettori con i grammi e il valore in volt di campioni per la taratura"""

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

    n = 10
    samples = random_samples(data, n)
    gram = round(float(mass_name.split('-')[0]),2)
    mass_list = [gram for _ in range(n)]

    return riga,mass_list,samples


def random_samples(lista,n):
    '''mischia la lista e ne ritorna una fetta inziale di n elementi dato come parametro'''

    shuffle(lista)
    samples = lista[:n]

    return samples

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

    list_mass = []
    list_mean = []

    lista_m_of_m = []
    i = 1
    precedente = lista[0][0]
    for row in lista:

        attuale = row[0]
        if attuale > (precedente + 0.2) or i == len(lista):
            riga = [str(round(mean(list_mass), 2)), str(mean(list_mean)), str(stdev(list_mean))]
            lista_m_of_m.append(riga)
            list_mass.clear()
            list_mean.clear()
            precedente = attuale

        list_mass.append(attuale)
        list_mean.append(row[1])
        i += 1
    return lista_m_of_m

def histograms(lista):
    '''plotta gli istogrammmi delle medie grezze
    :param lista'''

    list_mass = []
    list_mean = []

    lista_m_of_m = []
    i = 1
    cartella = './istogrammi/'
    precedente = lista[0][0]
    i = 1
    for row in lista:
        attuale = row[0]
        if attuale > (precedente + 0.2) or i == len(lista):
            save_plot_histogram(list_mean,precedente,cartella)
            list_mass.clear()
            list_mean.clear()
            precedente = attuale
        list_mass.append(attuale)
        list_mean.append(row[1])
        i += 1
    return lista_m_of_m

def save_plot_histogram(lista,massa,cartella='istogrammi/'):

    plt.hist(lista)
    plt.title(f'Istogramma - medie = {massa}g')
    path = f'{cartella}{massa}g.jpg';
    plt.savefig(path)
    plt.show()