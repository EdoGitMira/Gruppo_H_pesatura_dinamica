from pathlib import Path
from matplotlib import pyplot as plt
from letturaFileDinanico import *
from Sub_list_methods import *
import numpy as np


url = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati'
url_name_velocity = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati/speed.txt'

path_testo = Path(__file__).parent / "../dati/Features/Statiche"


def plot_data(lista):
    plt.plot(lista[0],lista[1], color="red", linewidth=1)
    plt.plot(lista[0], lista[2], color="black", linewidth=0.5)
    plt.plot(lista[0], lista[3], color="black", linewidth=0.5)
    plt.plot(lista[0], lista[4], color="blue", linewidth=1)
    plt.legend(['data','FTC1','FTC2','dataFiltered'])
    plt.xlabel('time [s]')
    plt.ylabel('signal [V]')
    plt.show()



def lista_features_dinamico(url_repo, url_name):  # read all file from git hub and calculate the feature static
    lista = creazione_numeri_dinamici(urllib.request.urlopen('https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati/v1_45m-min_280/1081.74/1081.74-26-11-10-34-41.txt'),'1081-4.txt')
    return lista

'''bisogna fare delle modifiche nella lettura ha smesso di funzionare correttamente'''


if __name__ == '__main__':

    #celle = pd.read_csv('1225.95-26-11-11-16-40.txt', sep='\t')
    lista = lista_features_dinamico(0,0)
    plot_data(lista)
    #lista = lista_features_dinamico(url, url_name_velocity)
    [l_piccola,l_grande,l_no_dim,salita,discesa] = split_list(lista)
    [media,std] = tratto_costante(l_piccola)



