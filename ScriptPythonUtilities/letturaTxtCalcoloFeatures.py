"""questo file serve per la lettura dei file txt e successivo calcolo della media e della deviazione
standard del singolo file"""

import os

path = "D:\repository\Progetto_Laboratorio_Misure_pesatura_dinamica\dati\taratura"


# Change the directory
os.chdir(path)
  
# Read text File
  
  
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())
  
  
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
  
        # call read text file function
        read_text_file(file_path)