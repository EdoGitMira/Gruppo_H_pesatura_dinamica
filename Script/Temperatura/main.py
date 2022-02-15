# This is a sample Python script.
import Function
import testmisura
import os
import letturaFileDinanico


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\ninsert the url of the github folder where is the data")
    url_folder=str(input())
    print("insert the folder where the file will be stored")
    folder=str(input())
    path_parent=os.getcwd()
    path=os.path.join(path_parent,folder)
    try:
        os.mkdir(path)
    except:
        f=0
    letturaFileDinanico.lista_features_dinamico(url_folder,folder,path_parent)




