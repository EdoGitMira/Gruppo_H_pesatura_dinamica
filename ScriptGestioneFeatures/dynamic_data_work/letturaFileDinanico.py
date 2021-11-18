import urllib
from urllib import request

def read_names_url_txt(url):
    names = []
    for element in urllib.request.urlopen(url):
        names.append(element.decode('utf-8').strip('\n'))
    return names


def lista_features_dinamico(url_repo, url_name):  # read all file from git hub and calculate the feature static
    '''VA CORRETTO'''
    velocity_name = read_names_url_txt(url_name)
    data = []

    for i in range(1,len(velocity_name)):  # read all file names velocity
        url_mass = url_repo + '/' + velocity_name[i] + '/mass.txt'
        mass = read_names_url_txt(url_mass)
        data_mass = []
        print('load file with velocity \t' + velocity_name[i])

        for mass_file in mass:  # read all file names in velocity for each kind of mass
            print('catchment mass \t' + mass_file)
            url_github = url_repo + '/' + velocity_name[i] + '/' + mass_file
            lista = creazione_numeri_dinamici(urllib.request.urlopen(url_github), mass_file)

        print("")
        data.append(lista)
    return lista



def creazione_numeri_dinamici(file, mass_name):
    """in questo prendiamo il file txt lo spezziamo più volte in modo da leggere tutti i dati dinmici, massa, FC1, FC2 e massa filtrata,  ritorna
    i 4 valori letti """
    masses = []
    FC1s = []
    FC2s = []
    masses_filt = []
    data = [0,0,0,0,0]
    for (i, element) in enumerate(file):
        if i > 4:
            element = element.decode('utf-8')
            for index in range(1,5):
                data[index] = crea_numero(element,index)

    masses.append(data[1])
    FC1s.append(data[2])
    FC2s.append(data[3])
    masses_filt.append(data[4])
    lista = [masses,FC1s,FC2s,masses_filt]

    return lista


def crea_numero(element,i):
    bridge = element.split('\t')[i].split('\n')[0].split('E')
    base = float(bridge[0].replace(',', '.'))  # number without exponent
    exponent = int(bridge[1])  # exponent of number
    number = round(base * pow(10, exponent), 10)
    return number
