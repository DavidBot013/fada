#!/usr/bin/env python3
import aux

""" 
Ordena las escenas que ocurren en la apertura.
opening: lista, contiene las escenas de la apertura.
N: entero, máxima grandeza.
animals_dict: diccionario, mapea animales a grandezas, ej: {animal:grandeza}
"""
def sort_opening_scenes(opening, N, animals_dict):
    sorted_opening = []
    for scene in opening:
        tuple = [(animal, animals_dict[animal]) for animal in scene]
        sorted_opening.append(aux.sort(tuple,N))
        
    return sorted_opening 
    
""" 
Reemplaza las escenas de las m-1 partes por sus contrapartes ya ordenadas.
parts: lista que contiene todas las partes.
N: entero, grandeza máxima.
animals_dict: diccionario que mapea animales a sus grandezas.
"""
def sort_rest_of_scenes(parts, N, animals_dict):  
    sorted_scenes = sort_opening_scenes(parts[0], N, animals_dict)
    # Constuir el diccionario.
    mapping = {str(scene):sorted_scenes[i] for i,scene in enumerate(parts[0])}
    
    for _part in parts[1:]: # parts[1:] es todas las partes sin la apertura. 
        for k,scene in enumerate(_part): # O((M-1)*K), K escenas en las partes posteriores a la apertura.
            _part[k] = mapping[str(scene)]
    
    parts[0] = sorted_scenes

"""
Ordena las partes del evento en orden ascendente de acuerdo a su grandeza.
parts: lista que contiene todas las partes.
animals_to_greatness: diccionario que mapea animales a grandezas.
"""
def sort_parts(parts, animals_to_greatness):
    scenes_to_greatness = {}
    scenes_with_greatness = []
    for scene in parts[0]: # O((m-1)k
        total = sum((animals_to_greatness[animal] for animal in scene))
        scenes_to_greatness[str(scene)] = total
        scenes_with_greatness.append((scene, total))

    k = max(scenes_to_greatness.values())
    parts[0] = aux.sort(scenes_with_greatness, k)

    for j,part in enumerate(parts[1:]): # O(m-1)
        scenes_with_greatness = [] # Tupla con las parejas (escena,grandeza)

        for scene in part: # O((m-1)k) 
            scenes_with_greatness.append((scene, scenes_to_greatness[str(scene)])) 

        parts[j+1] = aux.sort(scenes_with_greatness, k) 
        #draws = aux.check_for_draws(parts[j], scenes_greatness)
        #if draws: 
        #    solve_draws(parts[j], animals_to_greatness, draws)


"""
Busca empates en las escenas dadas y los resuelve.
scenes: lista de escenas con su grandeza
animals_to_greatness: Diccionario {animal:grandeza}
"""
def solve_draws(scenes, animals_to_greatness, draws):
    result = []
    animals_to_scenes = {}
    x = []
    for scene in scenes: # O((m-1)k) ó O(k)    
        animal = scene.pop()
        x.append((animal, hash_table[animal])) # O(1) 
        animals_to_scenes = {animal:scene}

    aux.sort(x)
