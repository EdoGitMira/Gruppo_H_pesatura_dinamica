import pickle
import Function
raw_name=2
raw_delta_t=1
raw_initial_time=0
raw_begin_data=3
print("name of folder where is the data")
folder_name=str(input())
print("Name of file to be open (without \".txt\")")
name_file=str(input())
file=open(folder_name + "/" + name_file + ".txt", "rb")
lista=pickle.load(file)
masses=[]
for name_mass in lista:     #scorro le cartelle delle masse
    file=open(folder_name + "/" + name_file + "/" + name_mass, "rb")
    mass=pickle.load(file)
    files=[]
    for mass_name in mass:       #scorre i file dentro alle cartelle delle masse
        file = open(folder_name + "/" + name_file + "/" + name_mass.replace(".txt","") +"/"+mass_name, "rb")
        mass_file=pickle.load(file)
        raws = []
        bridge = 0
        ftc2 = 0
        time = 0
        fallingEdge = False
        previousVal = 0
        if len(mass_file[0]) > 4:
            for (i,raw) in enumerate(mass_file):  #lettura delle singole pesate
                if i == raw_initial_time:
                    raws.append(raw[0])
                elif i == raw_delta_t:
                    raws.append(raw[0])
                elif i == raw_name:
                    bridge=raw.index("Bridge (Filtered)")
                    ftc2=raw.index("FTC2")
                    time=raw.index("time")
                elif i == raw_begin_data:
                    raws.append(raw[5:])
                elif i > raw_begin_data:
                    if fallingEdge:
                        raws.append([raw[time],raw[bridge]])
                    elif raw[ftc2]-previousVal>4:
                        fallingEdge=True
                    else:
                        previousVal=raw[ftc2]
            files.append(raws)
    masses.append(files)
file=open(folder_name+"/"+name_file+"_TMP.txt","wb")
pickle.dump(masses,file)