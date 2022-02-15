
#from CalcoloFeatures import *
from math import *
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def splpit_pandas(f,column,n):
    f[column] = [x.replace(',', '.') for x in f[column]]
    l = f[column].tolist()
    l = l[n:]
    l = np.float_(l)
    return l

def lettura_file_N(path,n,delimeter=';'):
    '''Legge il file e ritorna un numpy array
    :returns LISTA
    '''
    l = []
    f = pd.read_csv(path, delimiter = delimeter)
    i = 0
    for column in f.columns:
        if i > 0:
            a = splpit_pandas(f,column,n)
            l.append(a)
        i += 1
    return l

def medie_mobili(voltage,N):
    '''calcola la media mobile su N dati del file passato, ritorna un numpy array
    di una sola colonna con le media mobile
    :returns LISTA_MEDIE'''
    return np.convolve(voltage, np.ones(N) / N, mode='valid')

def plot_data(lista,title,path):
    plt.plot(lista)
    plt.title(title)
    plt.savefig(path)
    plt.show()

def plot_multiple_data(lista,title,legend,path):
    for i in lista:
        plt.plot(i)
    plt.title(title)
    plt.savefig(path)
    plt.show()


def write_csv_txt(lista,path = 'dati_Prove/medieMobili',_delimeter='\n',_header='Media Mobile su 30sec'):
    pathtxt = path + '.txt'
    pathcsv = path + '.csv'
    np.savetxt(pathtxt, lista, delimiter=_delimeter, header=_header)
    np.savetxt(pathcsv, lista, delimiter=_delimeter, header=_header)


'''
n = 6
path_dati = 'dati_Prove/prova_temp-29-11-14-06-15.csv'
l = lettura_file_N(path_dati,n,';')
plot_data(l[0],'Cella di Carico','peso.jpg')
plot_multiple_data(l[1:],'Temperature',['env','cell'],'tCells.jpg')
'''


'''
voltage = lettura_file('dati_Prove/test1-26-11-09-29-00.csv')
voltage1 = lettura_file('dati_Prove/1081.74-26-11-10-45-24.csv')
N = 60000
mobile = medie_mobili(voltage,N)
mobile1 = medie_mobili(voltage1,N)

plot_data(mobile)
plot_data(mobile1)
'''



'''
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
'''


