from pathlib import Path

import pandas as pd
from matplotlib import pyplot as plt
from letturaFileDinanico import *
from workonlist import *
import numpy as np



url = 'https://raw.githubusercontent.com/EdoGitMira/Gruppo_H_pesatura_dinamica/main/dati/'
url_name_velocity = 'https://raw.githubusercontent.com/EdoGitMira/Gruppo_H_pesatura_dinamica/main/dati/speed.txt'

path_testo = Path(__file__).parent / "../dati/Features/Statiche"


def plot_data(lista):
    plt.plot(lista[0],lista[1], color="red", linewidth=1)
    plt.plot(lista[0], lista[2], color="black", linewidth=0.5)
    plt.plot(lista[0], lista[3], color="black", linewidth=0.5)
    plt.plot(lista[0], lista[4], color="blue", linewidth=1)
    plt.legend(['data','FTC1','FTC2','dataFiltered'])
    plt.xlabel('time [s]')
    plt.ylabel('signal [V]')
    plt.xticks(20)
    plt.yticks(20)
    plt.show()

path = 'prova.csv'

def scrittura_csv(dati,velocita = 'v1',path = ''):

    for (i,elemento) in enumerate(dati):
        df = pd.DataFrame(dati, columns=['peso'+str(i+1)])
    df.to_csv(path,sep=";")

def estrapola_lista(lista_v, medie_v, pesi_v):

    for i in range(len(lista_v)):

        for j in range(len(lista_v[i])):

            for k in range(len(lista_v[j])):

                scrittura_csv(medie_v[i][j][k], pesi_v[i][j][k], 'v1', path)

def prima_colonna(pesi_v):
    col = []
    for pesi_c in pesi_v:

        for pesi in pesi_c:

            for peso in pesi:
                col.append(peso)

    return pd.DataFrame(col, columns=['peso_esatto'])

def N_colonne(liste_v):
    col = []
    nome_col = []
    for liste_c in liste_v:

        for liste in liste_c:

            for lista in liste:

                col.append(lista)

            nome_col.append('colonna')

    return pd.DataFrame(col, columns=['peso_esatto'])


if __name__ == '__main__':
    # celle = pd.read_csv('1225.95-26-11-11-16-40.txt', sep='\t')
    [df, df1, df2, df3, df4, df5, df6, df7] = lista_features_dinamico(url, url_name_velocity)
    #df7 = lista_features_dinamico(url, url_name_velocity)

    # estrapola_lista(lista,medie,pesi)

    name = 'dataset_interval_5_num.csv'
    df.to_csv(name, sep=';')
    print(df)

    name = 'dataset_interval_10_num.csv'
    df1.to_csv(name, sep=';')
    print(df1)

    name = 'dataset_interval_15_num.csv'
    df2.to_csv(name, sep=';')
    print(df2)

    name = 'dataset_interval_20_num.csv'
    df3.to_csv(name, sep=';')

    name = 'dataset_interval_25_num.csv'
    df4.to_csv(name, sep=';')

    name = 'dataset_interval_30_num.csv'
    df5.to_csv(name, sep=';')


    name = 'dataset_interval_35_num.csv'
    df6.to_csv(name, sep=';')

    name = 'dataset_interval_bestmedia_num.csv'
    df7.to_csv(name, sep=';')


    [df, df1, df2, df3, df4, df5, df6, df7] = lista_features_dinamico2(url,["v4_80m-min_782","v1_45m-min_280"])
    #df7 = lista_features_dinamico(url, url_name_velocity)

    # estrapola_lista(lista,medie,pesi)

    name = 'dataset_interval_5_num_v1v4.csv'
    df.to_csv(name, sep=';')
    print(df)

    name = 'dataset_interval_10_num_v1v4.csv'
    df1.to_csv(name, sep=';')
    print(df1)

    name = 'dataset_interval_15_num_v1v4.csv'
    df2.to_csv(name, sep=';')
    print(df2)

    name = 'dataset_interval_20_num_v1v4.csv'
    df3.to_csv(name, sep=';')

    name = 'dataset_interval_25_num_v1v4.csv'
    df4.to_csv(name, sep=';')

    name = 'dataset_interval_30_num_v1v4.csv'
    df5.to_csv(name, sep=';')

    name = 'dataset_interval_35_num_v1v4.csv'
    df6.to_csv(name, sep=';')

    name = 'dataset_interval_bestmedia_num_v1v4.csv'
    df7.to_csv(name, sep=';')

    [df, df1, df2, df3, df4, df5, df6, df7] = lista_features_dinamico2(url, ["v2_447", "v3_615"])
    # df7 = lista_features_dinamico(url, url_name_velocity)

    # estrapola_lista(lista,medie,pesi)

    name = 'dataset_interval_5_num_v2v3.csv'
    df.to_csv(name, sep=';')
    print(df)

    name = 'dataset_interval_10_num_v2v3.csv'
    df1.to_csv(name, sep=';')
    print(df1)

    name = 'dataset_interval_15_num_v2v3.csv'
    df2.to_csv(name, sep=';')
    print(df2)

    name = 'dataset_interval_20_num_v2v3.csv'
    df3.to_csv(name, sep=';')

    name = 'dataset_interval_25_num_v2v3.csv'
    df4.to_csv(name, sep=';')

    name = 'dataset_interval_30_num_v2v3.csv'
    df5.to_csv(name, sep=';')

    name = 'dataset_interval_35_num_v2v3.csv'
    df6.to_csv(name, sep=';')

    name = 'dataset_interval_bestmedia_num_v2v3.csv'
    df7.to_csv(name, sep=';')

    # scrittura CSV con Pandas per Mila.
    # tre cicli for, quello più interno gli passi il vettore e scrivi il titolo della colonna basta, al for medio
    # una cartella di masse, e al for superiore una cartella di velocità.