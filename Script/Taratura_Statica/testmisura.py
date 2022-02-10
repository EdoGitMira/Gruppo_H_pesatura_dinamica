import os
from path import Path
from math import *
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def plot_data1(lista):
    plt.plot(lista[0],lista[1], color="red", linewidth=1)
    plt.plot(lista[0], lista[2], color="black", linewidth=0.5)
    plt.plot(lista[0], lista[3], color="black", linewidth=0.5)
    plt.plot(lista[0], lista[4], color="blue", linewidth=1)
    plt.legend(['data','FTC1','FTC2','dataFiltered'])
    plt.xlabel('time [s]',fontsize=15)
    plt.ylabel('signal [V]',fontsize = 15)
    plt.xticks(fontsize = 15)
    plt.yticks(fontsize=15)
    plt.show()

def splpit_pandas(f,column,n):
    f[column] = [x.replace(',', '.') for x in f[column]]
    l = f[column].tolist()
    l = l[n:]
    l = np.float_(l)
    return l

def lettura_file_N(n,path = 'dati_Prove/146.14-19-11-10-46-14.csv',delimeter=';'):
    '''Legge il file e ritorna un numpy array
    :returns LISTA
    '''
    l = []
    f = pd.read_csv(path, delimiter = delimeter)
    i = 0
    for column in f.columns:
        if i > 0 and i < 5:
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
    #plt.xticks(16)
    #plt.yticks(17)
    plt.legend(legend)
    #plt.savefig(path)
    plt.show()


def write_csv_txt(lista,path = 'dati_Prove/medieMobili',_delimeter='\n',_header='Media Mobile su 30sec'):
    pathtxt = path + '.txt'
    pathcsv = path + '.csv'
    np.savetxt(pathtxt, lista, delimiter=_delimeter, header=_header)
    np.savetxt(pathcsv, lista, delimiter=_delimeter, header=_header)

'''
n = 6
path_dati = 'dati_Prove/1410.12-19-11-12-55-23.csv'
l = lettura_file_N(n,path=path_dati,delimeter=';')
l[1] = l[1]/8
l[2] = l[2]/8
#plot_data(l[0],'Cella di Carico','peso.jpg')
#plot_multiple_data(l[:4],'Voltage',['Bridge','FTC1','FTC2','BridgeFiltered'],'io.csv')
t = 0.000620
time = 0
a = [0 for i in range(len(l[0]))]
for i in range(0,len(l[0])):
    a[i] = time
    time += t

l.insert(0,a)
plot_data1(l)
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


