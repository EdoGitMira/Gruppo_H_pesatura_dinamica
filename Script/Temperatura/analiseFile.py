import matplotlib.pyplot as plt
import numpy as np
import chart_studio.plotly as py
import plotly.express as px

import Function

import datetime
import PT100
termometer=PT100.PT100()
temp_index=2
volt_index=3
temp_cell_ind=1
temp_env_ind=0
volt_mean_ind=0
volt_std_mean_ind=1
volt_std_ind=2
volt_time_ind=3
temp_env=[]
temp_cell=[]
volt_cell=[]
volt_std_mean=[]
volt_std=[]
time=[]
initial_time=datetime.datetime.now()
if not Function.digital_question("have you already processed the data?"):
    list=Function.open_data()
    for element in list:
        temp_env.append(element[temp_index][temp_env_ind])
        temp_cell.append(element[temp_index][temp_cell_ind])
        volt_cell.append(element[volt_index][volt_mean_ind])
        volt_std_mean.append(element[volt_index][volt_std_mean_ind])
        volt_std.append(element[volt_index][volt_std_ind])
        time.append(element[volt_index][volt_time_ind])
        if initial_time>element[volt_index][volt_time_ind]:
            initial_time=element[volt_index][volt_time_ind]
    if Function.digital_question("Do yow want to remove voltage outliers?"):
        indexes=Function.remove_outliers(volt_cell)
        if len(indexes) > 0:
            for i in sorted(indexes,reverse=True):
                del volt_cell[i]
                del temp_cell[i]
                del temp_env[i]
                del volt_std_mean[i]
                del volt_std[i]
                del volt_std[i]
    elif Function.digital_question("Do you want to remove value under the limit?"):
        print("What is the limit?")
        limit=float(input())
        indexes=Function.remove_under(volt_cell,limit)
        if len(indexes) > 0:
            for i in sorted(indexes,reverse=True):
                del volt_cell[i]
                del temp_cell[i]
                del temp_env[i]
                del volt_std_mean[i]
                del volt_std[i]
                del time[i]
    Function.save_data([temp_env,temp_cell,volt_cell,volt_std_mean,volt_std,time,initial_time])
else:
    list = Function.open_data()
    temp_env=list[0]
    temp_cell=list[1]
    volt_cell=list[2]
    volt_std_mean=list[3]
    volt_std=list[4]
    time=list[5]
    initial_time=list[6]
print(initial_time)
if Function.digital_question("Do you want to plot data?"):
    # plt.scatter(temp_env,volt_cell)
    # plt.xlabel("temperature envirornment")
    # plt.ylabel("cell voltage")
    # plt.show()
    # plt.scatter(temp_cell,volt_cell)
    # plt.xlabel("temperature cell")
    # plt.ylabel("cell voltage")
    # plt.show()
    plt.scatter(temp_cell,temp_env)
    plt.xlabel("Temperatura LC [°C]",fontsize=18)
    plt.ylabel("Temperatura ambiente [°C]",fontsize=18)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.show()
    # plt.scatter(volt_std_mean,volt_cell)
    # plt.xlabel("standrd deviation voltage mean")
    # plt.ylabel("cell voltage")
    # plt.show()
    # plt.scatter(volt_std,volt_cell)
    # plt.xlabel("mean standrd deviation voltage")
    # plt.ylabel("cell voltage")
    # plt.show()
    # ax = plt.axes(projection='3d')
    # time_sec = [(el - initial_time).total_seconds() for el in time]
    # ax.scatter3D(temp_cell, temp_env, time_sec)
    # ax.set_xlabel("cell temperature")
    # ax.set_ylabel("env temperature")
    # ax.set_zlabel("time")
    # plt.show()
    time_sec = [(el - initial_time).total_seconds() for el in time]
    ax = plt.axes(projection='3d')
    ax.scatter3D(time_sec,volt_std_mean,volt_cell)
    ax.set_xlabel("cell temperature")
    ax.set_ylabel("volt standard deviation mean")
    ax.set_zlabel("voltage")
    plt.show()
    # ax = plt.axes(projection='3d')
    # ax.scatter3D(temp_cell,volt_std,volt_cell)
    # ax.set_xlabel("cell temperature")
    # ax.set_ylabel("mean volt standard deviation")
    # ax.set_zlabel("voltage")
    # plt.show()
    time_sec = [(el - initial_time).total_seconds() for el in time]
    mass_cell = [el * 5191.421 - 4874.38 for el in volt_cell]
    df = px.data.iris()
    scatter=px.scatter_3d(df,temp_cell,time_sec,mass_cell)
    data=[scatter]
    scatter.show()
    #py.iplot(scatter, filename='jupyter-parametric_plot')

    ax = plt.axes(projection='3d')

    ax.scatter3D(temp_cell,time_sec,mass_cell)
    ax.set_xlabel("Temperature [°C]",fontsize=18,labelpad=20)
    ax.set_ylabel("Time [s]",fontsize=18,labelpad=20)
    ax.set_zlabel("Mass [g]",fontsize=18,labelpad=20)
    opt=ax.tick_params(labelsize="large")
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    for t in ax.zaxis.get_major_ticks(): t.label.set_fontsize(18)
    plt.show()
if Function.digital_question("Do you want to make linear regression?"):
    if Function.digital_question("Do you want to eliminate element after a date in second?"):
        print("date in second")
        times=int(input())
        time_sec = [(el - initial_time).total_seconds() for el in time]
        indexes=Function.remove_time(time_sec,times)
        for i in sorted(indexes,reverse=True):
            del volt_cell[i]
            del temp_cell[i]
    mass_cell=[el*5191.421-4874.38 for el in volt_cell]
    model=Function.linear_regression(temp_cell,mass_cell)
    print(model.coef_)
    print(model.intercept_)
    y=model.predict(np.array(temp_cell).reshape(-1,1))
    plt.scatter(temp_cell,mass_cell)
    plt.plot(temp_cell,y,color='r')
    plt.xlabel("Temperatura LC [°C]",fontsize=18)
    plt.ylabel("Massa [g]",fontsize=18)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.legend(["Valori di precarico dinamico"],loc='upper left',fontsize=18)
    plt.show()