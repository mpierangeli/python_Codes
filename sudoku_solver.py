import numpy as np
from collections import Counter

def check_constraints(sdk):
    if 0 in sdk: 
        return False
    for fila in sdk:
        if max(Counter(fila).values()) > 1:
            return False
    for fila in sdk.T:
        if max(Counter(fila).values()) > 1:
            return False
    for n in range(0,3):
        for m in range(0,3):
            bloque = sdk[3*n:3*(n+1)][:,3*m:3*(m+1)]
            bloque = bloque.reshape(1,9)
            for bloq in bloque:
                if max(Counter(bloq).values()) > 1:
                    return False
    return True

def ver(sdk):
    '''Muestra el Sudoku'''
    print("-------------------")
    for n in sdk:
        print(n)
    print("-------------------")
    return

def fuerza_bruta(sdk):
    '''Resuelve el sudoku probando todas las combinaciones posibles'''
    mask = sdk>0
    while check_constraints(sdk) == False:

    return
   

with open("sud_1_s.txt","r") as f:
    sudo = np.array(list(f.read()),dtype="int8")
sudo = np.reshape(sudo,(9,9))


ver(sudo)
print(check_constraints(sudo))