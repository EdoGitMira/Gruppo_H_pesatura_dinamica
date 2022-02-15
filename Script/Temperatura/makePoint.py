import pickle
import math
import numpy
import Function as fn
lista=fn.open_data()
values=[]
for mass in lista:
    for file in mass:
        value=math.floor((len(file)-3)/6)
        mediaStd=file[:3]   #insert the temperature in the first place of the element
        volt = [raw[1] for raw in file[4:]]
        time = file[4][0]
        mean = []
        std = []
        for i in range(6):
            start=3+value*i
            stop=value+3+value*i
            mean.append(numpy.mean(volt[start:stop]))
            std.append(numpy.std(volt[start:stop]))
        indexes=fn.remove_outliers(mean)
        if len(indexes)>0:
            mean.remove([mean[i] for i in indexes])
            std.remove([std[i] for i in indexes])
        indexes=fn.remove_outliers(std)
        if len(indexes)>0:
            mean.remove([mean[i] for i in indexes])
            std.remove([std[i] for i in indexes])
        std_mean=numpy.std(mean)
        mean=numpy.mean(mean)
        std=numpy.mean(std)
        mediaStd.append([mean,std_mean,std,time])    #insert mean, std_mean and std in the second element
        values.append(mediaStd)
fn.save_data(values)