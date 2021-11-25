from CalcoloFeatures import *
from math import *
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


url = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati'
url_name_velocity = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati/speed.txt'



def medieTemporalei(voltage, n):
    list_div = [mean(voltage[i * n:(i + 1) * n]) for i in range((len(voltage) + n - 1) // n)]
    return list_div

f = pd.read_csv('348.06-25-11-11-59-09.csv',delimiter=';')
f['Bridge'] = [x.replace(',', '.') for x in f['Bridge']]

voltage = f.Bridge.to_list()
voltage = voltage[3:]
voltage = np.float_(voltage)
N = 60000
lista_medie = np.convolve(voltage, np.ones(N)/N, mode='valid')

#lista_medie = medieTemporalei(voltage,n)

plt.plot(lista_medie)
plt.show()
plt.title('media mobile')




