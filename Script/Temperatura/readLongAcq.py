import letturaFileDinanico
import Function
import urllib
import PT100
termometer=PT100.PT100()
volt=[]
temp_cell=[]
temp_env=[]
time=[]
time_for_mm=[]
if not Function.digital_question("Do you have already process the data?"):
    print("insert the file url yow want to read")
    url_file=str(input())
    file=urllib.request.urlopen(url_file)
    list=letturaFileDinanico.create_list(file,5,2,4,1)
    print("lettura...")
    for element in list[3:]:
        time.append(element[0])
        volt.append(element[1])
        if element[2]>103 and element[3]>103:
            temp_env.append(termometer(element[2]).min())
            temp_cell.append(termometer(element[3]).min())
    print("procesing...")
    volt_mean = Function.mobile_mean(volt, 5000)
    time_for_mm=time[:len(time)-5000]
    temp_env = Function.normalize_list(temp_env, time)
    temp_cell = Function.normalize_list(temp_cell, time)
    print("saving...")
    Function.save_data([volt,temp_env,temp_cell,volt_mean,time,time_for_mm])
else:
    list = Function.open_data()
    volt = list[0]
    temp_env = list[1]
    temp_cell = list[2]
    volt_mean = list[3]
    time = list[4]
    time_for_mm = list[5]
Function.plot_data(time_for_mm,volt_mean,"time","voltage")
Function.plot_data(time,temp_cell,"time","cell temperature")
Function.plot_data(time,temp_env,"time","envirornment temperature")
temp_cell=temp_cell[:len(temp_cell)-5000]
Function.plot_data(temp_cell,volt_mean,"cell temperature","voltage")
if Function.digital_question("Do you want to make linear regression?"):
    model=Function.linear_regression(temp_cell,volt_mean)
    print(model.coef_)
    print(model.intercept_)