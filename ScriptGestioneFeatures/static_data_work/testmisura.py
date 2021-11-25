from PreparazioneFile import *
from math import *
from matplotlib import pyplot as plt

nome = '20g.txt'
url = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati'
url_name_velocity = 'https://raw.githubusercontent.com/EdoGitMira/Progetto_Laboratorio_Misure_pesatura_dinamica/main/dati/speed.txt'



def medieTemporalei(voltage, n):
    list_div = [mean(voltage[i * n:(i + 1) * n]) for i in range((len(voltage) + n - 1) // n)]
    return list_div


#[lista,grams,voltage] = lista_features_statico(url,url_name_velocity)

voltage = [uniform(0.000986,0.000988) for i in range(20000)]
lista_medie = medieTemporalei(voltage,2000)

plt.plot(lista_medie)
plt.show()




