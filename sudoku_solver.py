import numpy as np
from collections import Counter

def check_constraints(sdk):

    # if 0 in sdk: 
    #     return False
    # for fila in sdk:
    #     if max(Counter(fila).values()) > 1:
    #         return False
    # for fila in sdk.T:
    #     if max(Counter(fila).values()) > 1:
    #         return False
    for n in range(0,3):
        for m in range(0,3):
            bloque = sdk[3*n:3*(n+1)][:,3*m:3*(m+1)]
            
    return True

def fuerza_bruta(sdk):
    '''Resuelve el sudoku probando todas las combinaciones posibles'''
    for n in sdk:
        print(n)
    return sdk

with open("sud_1.txt","r") as f:
    sudo = np.array(list(f.read()),dtype="int8")
sudo = np.reshape(sudo,(9,9))
mask = sudo>0
print("-------------------")
fuerza_bruta(sudo)
print("-------------------")
print(check_constraints(sudo))
print(mask)