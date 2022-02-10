from statistics import *

class mass:

    '''
    name = 'null'
    static1 = [] ---> statica iniziale
    info1 = [] ---> info statica iniziale
    static2 = [] ---> statica finale
    info2 = [] ---> info statica finale

    list = [] ---> lista valori letti non filtrati
    list_f = [] ---> lista valori letti non filtrati

    fc1_up = [] fronti di salita fotocellula 1
    fc1_down = [] ---> fronti di discesa fotocellula 1
    fc2_up =  [] ---> fronti di salita fotocellula 2
    fc2_down = [] ---> fronti di discesa fotocellula 2
    '''

    name = 'null'
    dt = 0

    static1 = []
    info1 = []

    static2 = []
    info2 = []

    list = []
    list_f = []

    fc1_up = []
    fc1_down = []

    fc2_up = []
    fc2_down = []


    def __init__(self, name_init, list_init, list_initf, fc1, fc2, dt=0.000620):
        self.name = name_init
        self.dt = dt
        self.list = list_init
        self.list_f = list_initf
        self.static1 = list_init[0]
        self.static2 = list_init[-1]
        self.fc1_up =  self.fronti(fc1)
        self.info1 = self.methodinfo(self.static1)
        self.info2 = self.methodinfo(self.static2)

    def methodinfo(self, static):

        media = mean(static)
        dev_std = stdev(static)
        return [media, dev_std]

    def fronti(self, fronti):
        listaup = []
        listadown = []
        for lista in fronti:
            i = 0
            fronte_salita_FC = 0
            fronte_discesa_FC = 10
            for foto in lista:
                if foto > 8 and fronte_salita_FC == 0:
                    fronte_salita_FC = i
                if foto < 2 and fronte_salita_FC != 0:
                    fronte_discesa_FC = i
                    break
                i += 1
            listaup.append(fronte_salita_FC)
            listadown.append(fronte_discesa_FC)
        return listaup,listadown

    def split_list(self,lista):
        '''
        separa la lista passata in 3 liste:
        - lista tra fronte di salita FTC1 e discesa FTC2
        - lista tra fronte di discesa FT2 e salita FT1
        - lista tra frnte di discesa FTC1 e di discesa FTC2

        :returns: lista_centrale_grande, lista_centrale_piccola, lista_no_dim
       '''

        i = 0
        fronte_salita_FC1 = 0
        fronte_discesa_FC1 = 10
        for foto1 in lista[2]:
            if foto1 > 8 and fronte_salita_FC1 == 0:
                fronte_salita_FC1 = i
            if foto1 < 2 and fronte_salita_FC1 != 0:
                fronte_discesa_FC1 = i
                break
            i += 1

        fronte_salita_FC2 = 0
        fronte_discesa_FC2 = 10

        for foto2 in lista[3][fronte_discesa_FC1:]:

            if foto2 > 8 and fronte_salita_FC2 == 0:
                fronte_salita_FC2 = i
            if foto2 < 8 and fronte_salita_FC2 != 0:
                fronte_discesa_FC2 = i
                break
            i += 1

        lista_centrale_grande = [lista[1][fronte_salita_FC1:fronte_discesa_FC2],
                                 lista[4][fronte_salita_FC1:fronte_discesa_FC2]]
        lista_centrale_piccola = [lista[1][fronte_discesa_FC1:fronte_salita_FC2],
                                  lista[4][fronte_discesa_FC1:fronte_salita_FC2]]
        lista_no_dim = [lista[1][fronte_discesa_FC1:fronte_discesa_FC2],
                        lista[4][fronte_discesa_FC1:fronte_discesa_FC2]]
        salita = [lista[1][:fronte_salita_FC1], lista[4][:fronte_salita_FC1]]
        discesa = [lista[1][fronte_discesa_FC2:], lista[4][fronte_discesa_FC2:]]
        return lista_centrale_grande, lista_centrale_piccola, lista_no_dim, salita, discesa
