import numpy as np

def centrale_grande(lista):
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

    lista_centrale_grande = [lista[1][fronte_salita_FC1:fronte_discesa_FC2],lista[4][fronte_salita_FC1:fronte_discesa_FC2]]
    lista_centrale_piccola = [lista[1][fronte_discesa_FC1:fronte_salita_FC2],lista[4][fronte_discesa_FC1:fronte_salita_FC2]]
    lista_no_dim = [lista[1][fronte_discesa_FC1:fronte_discesa_FC2],lista[4][fronte_discesa_FC1:fronte_discesa_FC2]]

    return lista_centrale_grande, lista_centrale_piccola, lista_no_dim