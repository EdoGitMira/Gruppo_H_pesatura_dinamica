import os
import urllib
from urllib import request
from statistics import *
import pandas as pd
from pathlib import Path
import workonlist
from static_data_work.CalcoloFeatures import *

def read_names_url_txt(url):
    names = []
    for element in urllib.request.urlopen(url):
        names.append(element.decode('utf-8').strip('\n'))
    return names

def lista_features_dinamico(url_repo, url_name, numero=5, N = 6000):  # read all file from git hub and calculate the feature static and dinamic

    velocity_name = read_names_url_txt(url_name)
    n = 0
    data_v = []
    medie_v = []
    pesi_v = []
    tot_tot = []
    tot_tot1 = []
    tot_tot2 = []
    tot_tot3 = []
    tot_tot4 = []
    tot_tot5 = []
    tot_tot6 = []
    tot_tot7 = []

    #velocity_name = velocity_name[-2:]
    for velocity in velocity_name:  # read all file names velocity
        url_cartella = url_repo + '/' + velocity + '/cartelle.txt'
        cartella = read_names_url_txt(url_cartella)
        print('load file with velocity \t' + velocity)
        vel = velocita(velocity)
        #cartella = cartella[-10:] # CANCELLARE
        data_c = []
        medie_c = []
        pesi_c = []

        #cartella = cartella[-3:-1]
        for mass_folder in cartella:  # read all file names in velocity for each kind of mass
            print('catchment mass \t' + mass_folder)
            url_mass = url_repo + '/' + velocity + '/' + mass_folder
            mass = read_names_url_txt(url_mass + '/mass.txt')

            liste = []
            listef = []
            lista1 = []
            lista2 = []

            lista1 = creazione_numeri_statici(urllib.request.urlopen(url_mass + '/' + mass[0]), mass_folder)
            lista2 = creazione_numeri_statici(urllib.request.urlopen(url_mass + '/' + mass[-1]), mass_folder)

            pesi = []
            lista = []
            listaf = []
            medie_mob = []
            medie_mob_f = []

            if len(mass) > 32:
                mass = mass[-30:-1]  # CANCELLARE
                #gestione outlier da trovare possibile metodo di campra
            else:
                mass = mass[1:-1]
            l = len(mass)

            for (i,mass_file) in enumerate(mass):
                tot = []
                tot1 = []
                tot2 = []
                tot3 = []
                tot4 = []
                tot5 = []
                tot6 = []
                tot7 = []

                media1 = mean(lista1[1]) * float(i + 1)
                media2 = mean(lista2[1]) * float(l - (i + 1))
                peso = float((media2 + media1) / float(l)) * 1000  # unità di misura Volt
                #if peso > 2:
                #    print("x")
                #else:
                #   print("ok")

                url_github = url_mass + '/' + mass_file
                lista = creazione_numeri_dinamici(urllib.request.urlopen(url_github), mass_folder)
                test = workonlist.split_list(lista)
                # [media, dev, lista,media_mobile] = workonlist.tratto_costante(test.lista_centrale_piccola,N)
                # [media, dev, listaf,media_mobile_f] = workonlist.tratto_costante(test.lista_centrale_piccola_f,N)

                # nome differente a quello che ritorna
                media_mobile_f = workonlist.tratto_costante_divisione_tempi(test.lista_centrale_piccola_f, 5) # modificare questo ogni data set.
                media_mobile_f1 = workonlist.tratto_costante_divisione_tempi(test.lista_centrale_piccola_f, 10)  # modificare questo ogni data set.
                media_mobile_f2 = workonlist.tratto_costante_divisione_tempi(test.lista_centrale_piccola_f, 15)  # modificare questo ogni data set.
                media_mobile_f3 = workonlist.tratto_costante_divisione_tempi(test.lista_centrale_piccola_f, 20)  # modificare questo ogni data set.
                media_mobile_f4 = workonlist.tratto_costante_divisione_tempi(test.lista_centrale_piccola_f, 25)  # modificare questo ogni data set.
                media_mobile_f5 = workonlist.tratto_costante_divisione_tempi(test.lista_centrale_piccola_f, 30)  # modificare questo ogni data set.
                media_mobile_f6 = workonlist.tratto_costante_divisione_tempi(test.lista_centrale_piccola_f, 35)  # modificare questo ogni data set.
                media_mobile_f7 = workonlist.tratto_costante_divisione_tempi2(test.lista_centrale_piccola_f, 5)  # modificare questo ogni data set.
                '''
                media_mobile_2 = media_mobile_f[0:1400]
                liste.append(lista)
                listef.append(listaf)
                '''
                #medie_mob_f.append(media_mobile_f)

                base = []
                # pesi.append(peso)
                base.append(str(n))
                base.append(str(peso))
                base.append(vel)

                tot = base + media_mobile_f
                tot1 = base + media_mobile_f1
                tot2 = base + media_mobile_f2
                tot3 = base + media_mobile_f3
                tot4 = base + media_mobile_f4
                tot5 = base + media_mobile_f5
                tot6 = base + media_mobile_f6

                base.append(str(media_mobile_f7))
                tot_tot.append(tot)
                tot_tot1.append(tot1)
                tot_tot2.append(tot2)
                tot_tot3.append(tot3)
                tot_tot4.append(tot4)
                tot_tot5.append(tot5)
                tot_tot6.append(tot6)
                tot_tot7.append(base)
            print(n)
            n = n + 1
            '''
            data_c.append(listef)
            medie_c.append(medie_mob_f)
            pesi_c.append(pesi)  
        data_v.append(data_c)
        medie_v.append(medie_c)
        pesi_v.append(pesi_c)
        '''
    df = pd.DataFrame(tot_tot)
    df1 = pd.DataFrame(tot_tot1)
    df2 = pd.DataFrame(tot_tot2)
    df3 = pd.DataFrame(tot_tot3)
    df4 = pd.DataFrame(tot_tot4)
    df5 = pd.DataFrame(tot_tot5)
    df6 = pd.DataFrame(tot_tot6)
    df7 = pd.DataFrame(tot_tot7)
    #return data_v, medie_v, pesi_v, df
    return df,df1,df2,df3,df4,df5,df6,df7
    #return df7

def lista_features_dinamico2(url_repo, velocity_name, numero=5, N = 6000):  # read all file from git hub and calculate the feature static and dinamic
    n = 0
    data_v = []
    medie_v = []
    pesi_v = []
    tot_tot = []
    tot_tot1 = []
    tot_tot2 = []
    tot_tot3 = []
    tot_tot4 = []
    tot_tot5 = []
    tot_tot6 = []
    tot_tot7 = []

    #velocity_name = velocity_name[-2:]
    for velocity in velocity_name:  # read all file names velocity
        url_cartella = url_repo + '/' + velocity + '/cartelle.txt'
        cartella = read_names_url_txt(url_cartella)
        print('load file with velocity \t' + velocity)
        vel = velocita(velocity)
        #cartella = cartella[-10:] # CANCELLARE
        data_c = []
        medie_c = []
        pesi_c = []

        #cartella = cartella[-3:-1]
        for mass_folder in cartella:  # read all file names in velocity for each kind of mass
            print('catchment mass \t' + mass_folder)
            url_mass = url_repo + '/' + velocity + '/' + mass_folder
            mass = read_names_url_txt(url_mass + '/mass.txt')

            liste = []
            listef = []
            lista1 = []
            lista2 = []

            lista1 = creazione_numeri_statici(urllib.request.urlopen(url_mass + '/' + mass[0]), mass_folder)
            lista2 = creazione_numeri_statici(urllib.request.urlopen(url_mass + '/' + mass[-1]), mass_folder)

            pesi = []
            lista = []
            listaf = []
            medie_mob = []
            medie_mob_f = []

            if len(mass) > 32:
                mass = mass[-30:-1]  # CANCELLARE
                #gestione outlier da trovare possibile metodo di campra
            else:
                mass = mass[1:-1]
            l = len(mass)

            for (i,mass_file) in enumerate(mass):
                tot = []
                tot1 = []
                tot2 = []
                tot3 = []
                tot4 = []
                tot5 = []
                tot6 = []
                tot7 = []

                media1 = mean(lista1[1]) * float(i + 1)
                media2 = mean(lista2[1]) * float(l - (i + 1))
                peso = float((media2 + media1) / float(l)) * 1000  # unità di misura Volt
                #if peso > 2:
                #    print("x")
                #else:
                #    print("ok")

                url_github = url_mass + '/' + mass_file
                lista = creazione_numeri_dinamici(urllib.request.urlopen(url_github), mass_folder)
                test = workonlist.split_list(lista)
                # [media, dev, lista,media_mobile] = workonlist.tratto_costante(test.lista_centrale_piccola,N)
                # [media, dev, listaf,media_mobile_f] = workonlist.tratto_costante(test.lista_centrale_piccola_f,N)

                # nome differente a quello che ritorna
                media_mobile_f = workonlist.tratto_costante_divisione_tempi(test.lista_centrale_piccola_f, 5) # modificare questo ogni data set.
                media_mobile_f1 = workonlist.tratto_costante_divisione_tempi(test.lista_centrale_piccola_f, 10)  # modificare questo ogni data set.
                media_mobile_f2 = workonlist.tratto_costante_divisione_tempi(test.lista_centrale_piccola_f, 15)  # modificare questo ogni data set.
                media_mobile_f3 = workonlist.tratto_costante_divisione_tempi(test.lista_centrale_piccola_f, 20)  # modificare questo ogni data set.
                media_mobile_f4 = workonlist.tratto_costante_divisione_tempi(test.lista_centrale_piccola_f, 25)  # modificare questo ogni data set.
                media_mobile_f5 = workonlist.tratto_costante_divisione_tempi(test.lista_centrale_piccola_f, 30)  # modificare questo ogni data set.
                media_mobile_f6 = workonlist.tratto_costante_divisione_tempi(test.lista_centrale_piccola_f, 35)  # modificare questo ogni data set.
                media_mobile_f7 = workonlist.tratto_costante_divisione_tempi2(test.lista_centrale_piccola_f, 5)  # modificare questo ogni data set.
                '''
                media_mobile_2 = media_mobile_f[0:1400]
                liste.append(lista)
                listef.append(listaf)
                '''
                #medie_mob_f.append(media_mobile_f)

                base = []
                # pesi.append(peso)
                base.append(str(n))
                base.append(str(peso))
                base.append(vel)

                tot = base + media_mobile_f
                tot1 = base + media_mobile_f1
                tot2 = base + media_mobile_f2
                tot3 = base + media_mobile_f3
                tot4 = base + media_mobile_f4
                tot5 = base + media_mobile_f5
                tot6 = base + media_mobile_f6

                base.append(str(media_mobile_f7))
                tot_tot.append(tot)
                tot_tot1.append(tot1)
                tot_tot2.append(tot2)
                tot_tot3.append(tot3)
                tot_tot4.append(tot4)
                tot_tot5.append(tot5)
                tot_tot6.append(tot6)
                tot_tot7.append(base)
            print(n)
            n = n + 1
            '''
            data_c.append(listef)
            medie_c.append(medie_mob_f)
            pesi_c.append(pesi)  
        data_v.append(data_c)
        medie_v.append(medie_c)
        pesi_v.append(pesi_c)
        '''
    df = pd.DataFrame(tot_tot)
    df1 = pd.DataFrame(tot_tot1)
    df2 = pd.DataFrame(tot_tot2)
    df3 = pd.DataFrame(tot_tot3)
    df4 = pd.DataFrame(tot_tot4)
    df5 = pd.DataFrame(tot_tot5)
    df6 = pd.DataFrame(tot_tot6)
    df7 = pd.DataFrame(tot_tot7)
    #return data_v, medie_v, pesi_v, df
    return df,df1,df2,df3,df4,df5,df6,df7
    #return df7



def velocita(vel):
    '''prende il nome della cartella e ritorna la velocita in m/s'''

    vel = vel.split('_')[1].split('m')[0]
    return vel

def creazione_numeri_statici(file, mass_name):
    """in questo prendiamo il file txt lo spezziamo più volte in modo da leggere tutti i dati statici,"""
    tempo = []
    masses = []

    step = 0
    for (i, element) in enumerate(file):

        if i > 4:
            element = element.decode('utf-8')

            masses.append(crea_numero(element,1,False))
            tempo.append(step * (i-5))
        elif i ==2:
            step = crea_numero(element.decode('utf-8'),1,False)

    return [tempo, masses]

def creazione_numeri_dinamici(file, mass_name):
    """in questo prendiamo il file txt lo spezziamo più volte in modo da leggere tutti i dati dinamici, massa, FC1, FC2 e massa filtrata,  ritorna
    i 4 valori letti """
    tempo = []
    masses = []
    FC1s = []
    FC2s = []
    masses_filt = []
    data = [0,0,0,0,0]

    for (i, element) in enumerate(file):

        if i > 4:
            element = element.decode('utf-8')
            for index in range(1,5):
                data[index] = crea_numero(element,index)
            tempo.append(0.000620 * (i-5))
            masses.append(data[1])
            FC1s.append(data[2])#togliere 8
            FC2s.append(data[3])
            masses_filt.append(data[4])

    lista = [tempo,masses,FC1s,FC2s,masses_filt]

    return lista

def crea_numero(element, i, dinamico = True):
    ''' prende in ingresso un element di tipo byte[] riga di txt e lo converte in flot'''
    if dinamico:
        bridge = element.split('\t')[i].split('\n')[0].split('E')
        '''
        problema per la temperatura da gestire qui 
        '''
        base = float(bridge[0].replace(',', '.'))  # number without exponent
        exponent = int(bridge[1])  # exponent of number
        number = round(base * pow(10, exponent), 10)
    else:
        number = float(element.split('\t')[1].replace(',', '.'))
    return number