# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from pathlib import Path

import CalcoloFeatures
import PlotFilesData
import PreparazioneFile


url = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati'
url_name_velocity = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati/speed.txt'

path_testo = Path(__file__).parent / "../dati/Features/Statiche"
file_name = "0-FeaturePesiSatici.txt"
complete_name = os.path.join(path_testo, file_name)

file_name_m_o_m = '1-FeaturePesiStaticiDiFeature.txt'
complete_name_m_o_m = os.path.join(path_testo, file_name_m_o_m)



def scrittura_txt(lista, nome_completo, intestazione=''):

    '''funziona tutto ma questa funzione messa nel file PreparazioneFile.py'''

    file = open(nome_completo,'w', encoding='utf-8')
    file.write(intestazione)
    file.write('\n')

    for riga in lista:
        for elemento in riga:
            for dato in elemento:
                file.write(''.join(dato))
                file.write('\t')
            file.write('\n')

    file.close()
    return None

def scrittura_txt_m_o_m(lista, nome_completo, intestazione=''):

    '''funziona tutto ma questa funzione messa nel file PreparazioneFile.py'''

    file = open(nome_completo,'w', encoding='utf-8')
    file.write(intestazione)
    file.write('\n')

    for riga in lista:
        for elemento in riga:
            file.write(elemento)
            file.write('\t')
        file.write('\n')

    file.close()
    return None



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    lista = PreparazioneFile.lista_features_statico(url, url_name_velocity)
    [masses, means, std_dev] = PreparazioneFile.file_reg(lista)
    PlotFilesData.prepare_arrays(masses, means, std_dev)



    intestazione = 'peso [g]' + '\t\t' + 'media [V]' + '\t\t' + 'std_dev [V]'
    scrittura_txt(lista, complete_name, intestazione)

    ordered_list = CalcoloFeatures.sort_multiple_means(masses, means, std_dev)
    list_means_of_means = CalcoloFeatures.mean_of_means(ordered_list)
    scrittura_txt_m_o_m(list_means_of_means ,complete_name_m_o_m ,intestazione)
