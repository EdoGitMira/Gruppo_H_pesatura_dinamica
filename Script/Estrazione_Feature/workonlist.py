import collections
from statistics import *

import numpy as np


def split_list(lista):
    '''separa la lista passata in 3 liste:\n
    - lista tra fronte di salita FTC1 e discesa FTC2
    - lista tra fronte di discesa FT2 e salita FT1
    - lista tra frnte di discesa FTC1 e di discesa FTC2
    :returns: lista_centrale_grande, lista_centrale_piccola, lista_no_dim
   '''
    i = 0
    fronte_salita_FC1 = 0
    fronte_discesa_FC1 = 10
    for foto1 in lista[2]:
        if foto1 > 8 and fronte_salita_FC1 == 0:
            fronte_salita_FC1 = i
        if foto1 < 2 and fronte_salita_FC1 != 0:
            fronte_discesa_FC1 = i
            break
        i += 1
    fronte_salita_FC2 = 0
    fronte_discesa_FC2 = 10
    for foto2 in lista[3][fronte_discesa_FC1:]:

        if foto2 > 8 and fronte_salita_FC2 == 0:
            fronte_salita_FC2 = i
        if foto2 < 8 and fronte_salita_FC2 != 0:
            fronte_discesa_FC2 = i
            break
        i += 1
    lista_centrale_grande = lista[1][fronte_salita_FC1:fronte_discesa_FC2]
    lista_centrale_grande_f = lista[4][fronte_salita_FC1:fronte_discesa_FC2]
    lista_centrale_piccola = lista[1][fronte_discesa_FC1:fronte_salita_FC2]
    lista_centrale_piccola_f = lista[4][fronte_discesa_FC1:fronte_salita_FC2]
    lista_no_dim = lista[1][fronte_discesa_FC1:fronte_discesa_FC2]
    lista_no_dim_f = lista[4][fronte_discesa_FC1:fronte_discesa_FC2]
    salita = lista[1][:fronte_salita_FC1]
    salita_f = lista[4][:fronte_salita_FC1]
    discesa = lista[1][fronte_discesa_FC2:]
    discesa_f = lista[4][fronte_discesa_FC2:]

    valori = collections.namedtuple("data",["lista_centrale_piccola", "lista_centrale_grande", "lista_no_dim", "salita", "discesa", "lista_centrale_piccola_f", "lista_centrale_grande_f", "lista_no_dim_f", "salita_f", "discesa_f"])
    return valori(lista_centrale_piccola, lista_centrale_grande, lista_no_dim, salita, discesa, lista_centrale_piccola_f, lista_centrale_grande_f, lista_no_dim_f, salita_f, discesa_f)

def tratto_costante(dati,N=0):
    '''prende i dati e considera solo il tratto 'costante' che indicativamente è gli ultimi 3/4 del vettore'''
    da = int(len(dati)/4)
    dati = dati[da:]
    media = mean(dati)
    std_dev = stdev(dati)
    if N > 1:
        media_mobile = moving_average(dati)
        return media,std_dev,dati,media_mobile
    return media, std_dev, dati

def tratto_costante_divisione_tempi(dati,numero_intervalli = 1):

    sep = int(len(dati)/numero_intervalli)
    medie_dev = []

    a = 0

    for indice in range(sep, len(dati)+1, sep):
        b = indice
        medie = mean(dati[a:b])
        if medie < 0.8:
            medie = medie * 1000
        medie_dev.append(medie)
        #medie_dev.append(stdev(dati[a:b]))
        a = b+1

    if len(medie_dev) > numero_intervalli:
        medie_dev = medie_dev[:numero_intervalli]

    return medie_dev


def tratto_costante_divisione_tempi2(dati,numero_intervalli = 1):
    sep = int(len(dati)/numero_intervalli)
    medie_dev = []
    dev = []
    a = 0
    for indice in range(sep,len(dati)+1,sep):
        b = indice
        medie_dev.append(mean(dati[a:b]))
        dev.append(stdev(dati[a:b]))
        a = b+1
    c = min(dev)
    indice2 = dev.index(c)
    medie = medie_dev[indice2]
    if medie < 0.8:
        medie = medie *1000
    return medie

def moving_average(a, n=30) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    a = ret[n - 1:] / n
    a_ = a.tolist()
    return a_

def remove_outliers(list,valore_esatto):
    isFinished=False
    copy=list.copy()
    indexes=[]
    while not isFinished:
        media=np.mean(copy)
        std=np.std(copy)*2
        isFinished=True
        for (i,el) in enumerate(list):
            el = mean(el)
            if (el>media+std or el<media-std) and el in copy:
                copy.remove(el)
                indexes.append(i)
                isFinished=False
    return copy,indexes

def is_outlier(lista,esatto):

    media = mean(lista)
    std_dev = stdev(lista)*2
    sup = esatto + std_dev
    inf = esatto- std_dev

    if  media < inf and media > sup:
        return True

    return False