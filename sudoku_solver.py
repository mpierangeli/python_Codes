import numpy as np

def fuerza_bruta(sdk):
    '''Resuelve el sudoku probando todas las combinaciones posibles'''

    for n in sdk:
        print(n)
    return sdk

with open("sud_1.txt","r") as f:
    sudo = np.array(list(f.read()),dtype="int8")
sudo = np.reshape(sudo,(9,9))
mask = sudo>0

fuerza_bruta(sudo)

