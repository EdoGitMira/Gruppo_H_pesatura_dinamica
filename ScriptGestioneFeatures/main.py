# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pathlib import Path
import PreparazioneFile

url = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati/taratura/'
url_name_velocity=''
url_name_mass=''
path = Path(__file__).parent / "../dati/taratura"  # path relativa quindi torna indietro e poi va avanti nelle cartelle definite.
intestazione = 'peso'+'\t'+'media'+'\t'+'std_dev'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lista = PreparazioneFile.lista_features_statico(url,path)

    file = open('prova.txt', "w", encoding='utf-8')
    file.write(intestazione)
    file.write('\n')

    for riga in lista:
        for elemento in riga:
            file.write(elemento)
            file.write('\t')
        file.write('\n')
    file.close()
