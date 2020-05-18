#!/usr/bin/env python3

# Implementación de Counting Sort
# Ordena una lista de tuplas en orden ascendente en O(n).
# Cada tupla tiene la forma (llave:valor) valor es un entero de 0 a k
def sort(lista, k):
    C = [0 for i in range(k+1)]
    B = [None for i in range(len(lista))]
    
    for j in range(len(lista)):
        C[lista[j][1]] += 1
    
    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]
    
    for j in range(len(lista)-1, -1,-1):
        index = C[lista[j][1]] - 1
        B[index] = lista[j][0] # B solo contiene los animales.
        C[lista[j][1]] -= 1

    return B

"""
Busca empates en las escenas de una parte y devuelve una lista de los indices de las escenas están en empate
scenes_to_greatness: diccionario que mapea escenas a grandezas
"""
def check_for_draws(scenes, greatness):
    start = 0
    end = 0
    draws = []
    for i,scene in enumerate(scenes):
        if i > 0 and greatness[i] == greatness[i-1]:
            if not start:
                start = i - 1
            end = i
        elif end != 0:
            draws.append((start, end))
            #for _scene in scenes[start, end+1]:

            start, end = 0,0

    return draws
