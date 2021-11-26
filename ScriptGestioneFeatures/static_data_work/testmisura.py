import os
from path import Path
from CalcoloFeatures import *
from math import *
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def lettura_file(path='dati_Prove/test-25-11-13-41-26.csv',delimeter=';'):
    '''Legge il file e ritorna un numpy array
    di una sola colonna con i valori acquisiti
    :returns LISTA_Voltage
    '''
    f = pd.read_csv(path, delimiter = delimeter)
    f['Bridge'] = [x.replace(',', '.') for x in f['Bridge']]
    voltage = f.Bridge.to_list()
    voltage = voltage[3:]
    voltage = np.float_(voltage)
    return voltage

def medie_mobili(voltage,N):
    '''calcola la media mobile su N dati del file passato, ritorna un numpy array
    di una sola colonna con le media mobile
    :returns LISTA_MEDIE'''
    return np.convolve(voltage, np.ones(N) / N, mode='valid')

def plot_data(lista,title = 'media_mobile'):
    plt.plot(lista)
    plt.show()
    plt.title(title)

def write_csv_txt(lista,path = 'dati_Prove/medieMobili',_delimeter='\n',_header='Media Mobile su 30sec'):
    pathtxt = path + '.txt'
    pathcsv = path + '.csv'
    np.savetxt(pathtxt, lista, delimiter=_delimeter, header=_header)
    np.savetxt(pathcsv, lista, delimiter=_delimeter, header=_header)

path_prima = 'dati_Prove/146.59-25-11-09-40-32.csv'
path_dopo = 'dati_Prove/146.59-25-11-09-46-34.csv'
N = 6000

voltage_prima = lettura_file(path_prima)
voltage_dopo = lettura_file(path_dopo)

media_prima = mean(voltage_prima)
media_dopo = mean(voltage_dopo)
std_dev_prima= stdev(voltage_prima)
std_dev_dopo = stdev(voltage_dopo)

nome = 'dati_Prove/146.59 Media'

lista_prima = [media_prima,std_dev_prima]
lista_dopo = [media_dopo,std_dev_dopo]
dati = [lista_prima,lista_dopo]
write_csv_txt(dati,nome,_delimeter='\t')




