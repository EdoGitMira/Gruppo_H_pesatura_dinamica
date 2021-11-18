
from static_data_work.PreparazioneFile import *


def lista_features_dinamico(url_repo, url_name):  # read all file from git hub and calculate the feature static
    '''VA CORRETTO'''
    velocity_name = read_names_url_txt(url_name)
    data = []
    for velocity in velocity_name:  # read all file names velocity
        url_mass = url_repo + '/' + velocity + '/mass.txt'
        mass = read_names_url_txt(url_mass)
        data_mass = []
        print('load file with velocity \t' + velocity)

        for mass_file in mass:  # read all file names in velocity for each kind of mass
            print('catchment mass \t' + mass_file)
            url_github = url_repo + '/' + velocity + '/' + mass_file
            [mass,FC1,FC2,mass_filt] = creazione_numeri_dinamici(urllib.request.urlopen(url_github), mass_file)

        print("")
        data.append(data_mass)
    return data

def creazione_numeri_dinamici(file, mass_name):
    """in questo prendiamo il file txt lo spezziamo più volte in modo da leggere tutti i dati dinmici, massa, FC1, FC2 e massa filtrata,  ritorna
    i 4 valori letti """
    data = []
    for (i, element) in enumerate(file):
        if i > 5:
            element = element.decode('utf-8')
            for index in range(1,5):
                data[index] = crea_numero(element,index)

    return data[1],data[2],data[3],data[4]


def crea_numero(element,i):
    bridge = element.split('\t')[i].split('\n')[0].split('E')
    base = float(bridge[0].replace(',', '.'))  # number without exponent
    exponent = int(bridge[i])  # exponent of number
    number = round(base * pow(10, exponent), 10)
    return number
