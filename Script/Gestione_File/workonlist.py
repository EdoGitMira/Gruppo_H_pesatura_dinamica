import collections

import numpy as np
from statistics import *
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

def tratto_costante(dati):
    '''prende i dati e considera solo il tratto 'costante' che indicativamente è gli ultimi 3/4 del vettore'''
    da = int(len(dati)/4)
    dati = dati[da:]
    media = mean(dati)
    std_dev = stdev(dati)
    return media,std_dev,dati