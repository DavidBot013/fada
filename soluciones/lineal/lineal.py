#!/usr/bin/env python3
#import aux
import cProfile

scenes_to_greatness = {}
""" 
Ordena las escenas que ocurren en la apertura.
opening: lista, contiene las escenas de la apertura.
N: entero, máxima grandeza.
animals_dict: diccionario, mapea animales a grandezas, ej: {animal:grandeza}
"""
def sortx_opening_scenes_locally(opening, N, animals_dict):
    sortxed_opening = []
    for scene in opening:
        tuple = [(animal, animals_dict[animal]) for animal in scene]
        sortxed_opening.append(sortx(tuple,N))
        
    return sortxed_opening 
    
""" 
Reemplaza las escenas de las m-1 partes por sus contrapartes ya ordenadas.
parts: lista que contiene todas las partes.
N: entero, grandeza máxima.
animals_dict: diccionario que mapea animales a sus grandezas.
"""
def sortx_rest_of_scenes_locally(parts, N, animals_dict):  
    sortxed_scenes = sortx_opening_scenes_locally(parts[0], N, animals_dict)
    # Constuir el diccionario.
    mapping = {str(scene):sortxed_scenes[i] for i,scene in enumerate(parts[0])}
    
    for _part in parts[1:]: # parts[1:] es todas las partes sin la apertura. 
        for k,scene in enumerate(_part): # O((M-1)*K), K escenas en las partes posteriores a la apertura.
            _part[k] = mapping[str(scene)]
    
    parts[0] = sortxed_scenes

"""
Ordena las escenad de las partes del evento en orden ascendente de acuerdo a su grandeza.
parts: lista que contiene todas las partes.
animals_to_greatness: diccionario que mapea animales a grandezas.
"""
def sortx_scenes(parts, animals_to_greatness):    
    scenes_with_greatness = [None] * len(parts[0])
    _scene = parts[0]
    for i in range(len(_scene)): # O((m-1)k
        total = animals_to_greatness[_scene[i][0]] + animals_to_greatness[_scene[i][1]] + animals_to_greatness[_scene[i][2]] 
        scenes_to_greatness[str(_scene[i])] = total
        scenes_with_greatness[i] = (_scene[i], total)

    k = max(scenes_to_greatness.values())
    parts[0] = sortx(scenes_with_greatness, k)

    for j,part in enumerate(parts[1:]): # O(m-1)
        _scenes_with_greatness = [] # Tupla con las parejas (escena,grandeza)

        for scene in part: # O((m-1)k) 
            _scenes_with_greatness.append((scene, scenes_to_greatness[str(scene)])) 

        parts[j+1] = sortx(_scenes_with_greatness, k) 
        #draws = aux.check_for_draws(parts[j], scenes_greatness)# O((m-1)k)
        #if draws: 
        #    solve_draws(parts[j], scenes_to_greatness, animals_to_greatness)
    
    #for i in range(1, len(parts)):
     #   parts[i] = sortx(scenes_with_greatness, k)

"""
Busca empates en las escenas dadas y los resuelve.
scenes: lista de escenas con su grandeza
animals_to_greatness: Diccionario {animal:grandeza}
"""
def solve_draws(draws, scenes, scenes_to_greatness, animals_to_greatness):
    scenes_with_max_great=[]
    x = []
    for pos in draws:
        x.append()

def sortx(lista, k):
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
Calcula que animales participaron más y en cuantas escenas
"""
def get_animal_ocurrences(all_scenes, animals, operator):
    animals_to_ocurrences = {animal:0 for animal in animals} 
    for scene in all_scenes: # O((m-1)k)
        animals_to_ocurrences[scene[0]] += 1
        animals_to_ocurrences[scene[1]] += 1
        animals_to_ocurrences[scene[2]] += 1


    
    candidate = operator(animals_to_ocurrences, key=animals_to_ocurrences.get)
    result = {candidate:animals_to_ocurrences[candidate]}

    for animal in animals_to_ocurrences:
        if animal is not candidate and animals_to_ocurrences[animal] == animals_to_ocurrences[candidate]:
            result[animal] = animals_to_ocurrences[animal]

    return result

def get_avg(all_scenes, scenes_to_greatness):
    total = 0
    for scene in all_scenes:
        total += scenes_to_greatness[str(scene)]

    return total/len(all_scenes)


