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

def lista_features_dinamico(url_repo, url_name):  # read all file from git hub and calculate the feature static and dinamic

    velocity_name = read_names_url_txt(url_name)
    data = []
    lista = []
    for velocity in velocity_name:  # read all file names velocity
        url_cartella = url_repo + '/' + velocity + '/cartelle.txt'
        cartella = read_names_url_txt(url_cartella)

        print('load file with velocity \t' + velocity)
        for (i,mass_folder) in enumerate(cartella):  # read all file names in velocity for each kind of mass
            print('catchment mass \t' + mass_folder)
            url_mass = url_repo + '/' + velocity + '/' + mass_folder
            mass = read_names_url_txt(url_mass + '/mass.txt')

            liste = []
            listef = []
            lista1 = []
            lista2 = []

            lista1 = creazione_numeri_statici(urllib.request.urlopen(url_mass + '/' + mass[0]), mass_folder)
            lista2 = creazione_numeri_statici(urllib.request.urlopen(url_mass + '/' + mass[-1]), mass_folder)

            media1 = mean(lista1[1])*float(i+1)
            media2 = mean(lista2[1])*float(30-(i+1))
            peso = float((media2+media1)/float(30))
            lista = []
            listaf = []
            for mass_file in mass[1:-1]:
                url_github = url_mass + '/' + mass_file
                lista = creazione_numeri_dinamici(urllib.request.urlopen(url_github), mass_folder)
                test = workonlist.split_list(lista)
                [media, dev, lista] = workonlist.tratto_costante(test.lista_centrale_piccola)
                [media, dev, listaf] = workonlist.tratto_costante(test.lista_centrale_piccola_f)
                liste.append(lista)
                listef.append(listaf)
            print("")
            data.append(liste)

    return lista


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