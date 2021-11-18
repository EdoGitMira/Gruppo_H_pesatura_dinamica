from pathlib import Path
from letturaFileDinanico import *

url = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati'
url_name_velocity = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati/speed.txt'

path_testo = Path(__file__).parent / "../dati/Features/Statiche"

if __name__ == '__main__':
    lista = lista_features_dinamico(url,url_name_velocity)
    print(lista)