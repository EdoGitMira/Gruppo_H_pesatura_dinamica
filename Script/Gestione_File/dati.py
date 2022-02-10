from pathlib import Path
from matplotlib import pyplot as plt
from letturafile import *
from workonlist import *
import numpy as np


url = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati'
url_name_velocity = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati/speed.txt'

path_repo = Path(__file__).parents[2]
path_dir = os.path.join(path_repo, "./dati/Features/Dinamiche")

file_name = "0-FeaturePesiSatici.txt"
complete_name = os.path.join(path_dir, file_name)

file_name_m_o_m = '1-FeaturePesiStaticiDiFeature.txt'
complete_name_m_o_m = os.path.join(path_dir, file_name_m_o_m)


def plot_data(lista):
    plt.plot(lista[0],lista[1], color="red", linewidth=1)
    plt.plot(lista[0], lista[2], color="black", linewidth=0.5)
    plt.plot(lista[0], lista[3], color="black", linewidth=0.5)
    plt.plot(lista[0], lista[4], color="blue", linewidth=1)
    plt.legend(['data','FTC1','FTC2','dataFiltered'])
    plt.xlabel('time [s]')
    plt.ylabel('signal [V]')
    plt.show()


if __name__ == '__main__':

    #celle = pd.read_csv('1225.95-26-11-11-16-40.txt', sep='\t')
    lista = lista_features_dinamico(url,url_name_velocity)
    plot_data(lista)
    #lista = lista_features_dinamico(url, url_name_velocity)
    [l_piccola,l_grande,l_no_dim,salita,discesa] = split_list(lista)
    [media,std] = tratto_costante(l_piccola)