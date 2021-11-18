from pathlib import Path

from matplotlib import pyplot as plt
from letturaFileDinanico import *
from Sub_list_methods import *
import numpy as np


url = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati'
url_name_velocity = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati/speed.txt'

path_testo = Path(__file__).parent / "../dati/Features/Statiche"

if __name__ == '__main__':
    lista = lista_features_dinamico(url, url_name_velocity)
    lista = np.array(lista)
    lista_centrale = centrale_grande(lista)
    print(lista)

def plot_data(lista):
    plt.plot(lista[0],lista[1], color="red", linewidth=1)
    plt.plot(lista[0], lista[2], color="black", linewidth=0.1)
    plt.plot(lista[0], lista[3], color="black", linewidth=0.1)
    plt.plot(lista[0], lista[4], color="blue", linewidth=1)
    plt.xticks(())
    plt.yticks(())
    plt.show()