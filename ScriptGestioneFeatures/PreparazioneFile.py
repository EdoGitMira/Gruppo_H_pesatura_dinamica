import urllib
from os import *
# noinspection PyCompatibility
from pathlib import Path
# noinspection PyCompatibility
from urllib import request
from CalcoloFeatures import *

url = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati/Features/Statiche/0-FeaturePesiSatici.txt'




def lista_features_statico(url_repo, url_name):  # read all file from git hub and calculate the feature static
    velocity_name = read_names_url_txt(url_name)
    data = []
    for velocity in velocity_name:  # read all file names velocity
        url_mass = url_repo + '/v' + velocity + '/mass.txt'
        mass = read_names_url_txt(url_mass)
        data_mass = []
        print('load file with velocity \t' + velocity)

        for mass_file in mass:  # read all file names in velocity for each kind of mass
            print('catchment mass \t' + mass_file)
            url_github = url_repo + '/v' + velocity + '/' + mass_file
            row = calcolo_feature_statiche(urllib.request.urlopen(url_github), mass_file)
            data_mass.append(row)

        print("")
        data.append(data_mass)



    return data


def file_reg(lista):

    mass = []
    mean = []
    std_deviations = []

    for val in lista:
       for dati in val:
            mass.append([float(dati[0].split('-')[0])])
            mean.append(float(dati[1]))
            std_deviations.append(float(dati[2]))
    return mass,mean,std_deviations


def read_names_url_txt(url):
    names = []
    for element in urllib.request.urlopen(url):
        names.append(element.decode('utf-8').strip('\n'))
    return names
