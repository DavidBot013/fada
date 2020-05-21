#!/usr/bin/env python3
from collections import defaultdict
from itertools import chain
# Implementación de Counting Sort
# Ordena una lista de tuplas en orden ascendente en O(n).
# Cada tupla tiene la forma (llave:valor) valor es un entero de 0 a k
def sort(lista, k):
    if k > len(lista):
        lista += [('?', 0)]*(k-len(lista))

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
    
    return list(filter(lambda a: a != '?', B))

"""
Retorna una lista de las mayores grandezas individuales de cada animal entre escenas
que están empatadas.
list_of_scenes: una lista de las escenas que se encuentran en empate, ej: [[animal1, animal2, animal3], [animala, animalb, animalc]]
animals_to_greatness: una tabla hash que mapea animales a sus grandezas ej. {animal:grandeza}

Retorna una lista de tuplas con la que sort pueda trabajar, es decir, está función NO debe hacer ningún tipo de ordenamiento.
Su trabajo es retornar una lista de tuplas donde no haya duplicados en las grandezas [(escena, 7), (escena, 4)]
"""
def remove_duplicates(list_of_scenes, animals_to_greatness):
    
    x = [scene for scene in list_of_scenes]
    y = [animals_to_greatness[scene[-1]] for scene in list_of_scenes]
    
    i = 2 
    while i >= 0: 
        duplicates_index = list_duplicates(y) 
        if duplicates_index:
            i -= 1
            for index in duplicates_index:
                scene = x[index]
                y[index] = animals_to_greatness[scene[i]] 
        else:
            break
    
    return sort(list(zip(x,y)), max(y))

def list_duplicates(lst, pack=False):
    D = defaultdict(list)
    for i, item in enumerate(lst):
        D[item].append(i)
    D = [v for v in D.values() if len(v) > 1]
    
    if pack:
        return D
    else:
        return list(chain.from_iterable(D))
