import os
import urllib
from urllib import request
import pickle
import pandas as pd
from pathlib import Path

import Function


def read_rows_url_txt(url):
    rows = []
    for element in urllib.request.urlopen(url):
        rows.append(element.decode('utf-8').strip('\n'))
    return rows


def lista_features_dinamico(url_repo,save_folder,path_parent):  # read all file from git hub

    velocity_name = read_rows_url_txt(url_repo+"/speed.txt")
    for velocity in velocity_name:  # read all file names velocity
        url_cartella = url_repo + '/' + velocity + '/cartelle.txt'
        cartella = read_rows_url_txt(url_cartella)
        path=os.path.join(path_parent,save_folder,velocity)
        os.mkdir(path)
        print('load file with velocity \t' + velocity)
        lista=[]
        for mass_folder in cartella:  # read all file names in velocity for each kind of mass
            print('catchment mass \t' + mass_folder)
            url_mass = url_repo + '/' + velocity + '/' + mass_folder
            mass = read_rows_url_txt(url_mass + "/mass.txt")
            masses=[]
            path_mass=os.path.join(path,mass_folder)
            os.mkdir(path_mass)
            for mass_file in mass:
                url_github = url_mass + '/' + mass_file
                data = create_list(urllib.request.urlopen(url_github),raw_begin_data=5,raw_delta_t=2,raw_initial_time=1,raw_colunm_name=4)
                file=open(save_folder+"/"+velocity+"/"+ mass_folder+"/"+mass_file,"wb")
                pickle.dump(data,file)
                masses.append(mass_file)
            fp=open(save_folder+"/"+velocity+"/"+ mass_folder+".txt","wb")
            pickle.dump(masses, fp)
            lista.append(mass_folder+".txt")
        fp=open(save_folder+"/"+velocity+".txt","wb")
        pickle.dump(lista,fp)



def creazione_numeri_dinamici(file, mass_name):
    """in questo prendiamo il file txt lo spezziamo più volte in modo da leggere tutti i dati dinamici, massa, FC1, FC2 e massa filtrata,  ritorna
    i 4 valori letti """
    tempo = []
    masses = []
    FC1s = []
    FC2s = []
    masses_filt = []
    temp = []
    for (i, element) in enumerate(file):

        if i > 4:
            element = element.decode('utf-8')
            data=convert_number(element)
            tempo.append(0.000620 * (i-5))
            if len(data)>1:
                masses.append(data[1])
            if len(data)>2:
                FC1s.append(data[2]/8)#togliere 8
            if len(data)>3:
                FC2s.append(data[3]/8)
            if len(data)>4:
                masses_filt.append(data[4])
            if len(data)>5:
                temp=data[5:6]

    lista = [tempo,masses,FC1s,FC2s,masses_filt,temp]
    lista.insert(0,mass_name)
    return lista


def create_list(file,raw_begin_data,raw_delta_t,raw_colunm_name,raw_initial_time):
    lista=[]
    for (i, element) in enumerate(file):
        element = element.decode('utf-8')
        if i == raw_colunm_name:
            data=element.split("\n")[0].split("\t")
            lista.append(data)
        elif i == raw_delta_t or i == raw_initial_time:
            data=element.split("\n")[0].split("\t")[1:]
            lista.append(data)
        elif i >= raw_begin_data:
            data=convert_number(element)
            lista.append(data)

    return lista

def crea_numero(element,i):
    bridge = element.split('\t')[i].split('\n')[0].split('E')
    base = float(bridge[0].replace(',', '.'))  # number without exponent
    exponent = int(bridge[1])  # exponent of number
    number = round(base * pow(10, exponent), 10)
    return number

def convert_number(string,delimeter='\t'):
    elements=string.split(delimeter)
    numbers=[]
    for el in elements:
        if not '/' in el:
            if 'E' in el:
                splited=el.split('E')
                base = float(splited[0].replace(',', '.'))  # number without exponent
                exponent = int(splited[1])  # exponent of number
                number = round(base * pow(10, exponent), 10)
        else:
            number=Function.read_date(el)     #dates
        numbers.append(number)
    return numbers