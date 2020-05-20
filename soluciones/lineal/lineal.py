#!/usr/bin/env python3
import aux
import cProfile

scenes_to_greatness = {}
""" 
Ordena las escenas que ocurren en la apertura.
opening: lista, contiene las escenas de la apertura.
N: entero, máxima grandeza.
animals_dict: diccionario, mapea animales a grandezas, ej: {animal:grandeza}
"""
def sort_opening_scenes_locally(opening, N, animals_dict):
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
def sort_rest_of_scenes_locally(parts, N, animals_dict):  
    sorted_scenes = sort_opening_scenes_locally(parts[0], N, animals_dict)
    # Constuir el diccionario.
    mapping = {str(scene):sorted_scenes[i] for i,scene in enumerate(parts[0])}
    
    for _part in parts[1:]: # parts[1:] es todas las partes sin la apertura. 
        for k,scene in enumerate(_part): # O((M-1)*K), K escenas en las partes posteriores a la apertura.
            _part[k] = mapping[str(scene)]
    
    parts[0] = sorted_scenes

"""
Ordena las escenad de las partes del evento en orden ascendente de acuerdo a su grandeza.
parts: lista que contiene todas las partes.
animals_to_greatness: diccionario que mapea animales a grandezas.
"""
def sort_scenes(parts, animals_to_greatness):    
    scenes_with_greatness = [None] * len(parts[0])
    _scene = parts[0]
    for i in range(len(_scene)): # O((m-1)k
        total = animals_to_greatness[_scene[i][0]] + animals_to_greatness[_scene[i][1]] + animals_to_greatness[_scene[i][2]] 
        scenes_to_greatness[str(_scene[i])] = total
        scenes_with_greatness[i] = (_scene[i], total)

    k = max(scenes_to_greatness.values())
    parts[0] = aux.sort(scenes_with_greatness, k)

    for j,part in enumerate(parts[1:]): # O(m-1)
        _scenes_with_greatness = [] # Tupla con las parejas (escena,grandeza)

        for scene in part: # O((m-1)k) 
            _scenes_with_greatness.append((scene, scenes_to_greatness[str(scene)])) 

        parts[j+1] = aux.sort(_scenes_with_greatness, k) 
    
        # Empates
        draws = aux.list_duplicates(list(zip(*_scenes_with_greatness))[1], True)# O(k)
        if draws:
            current_part = parts[j]
            for draw in draws: # O(k/2) en el peor caso.
                start, end = draw[0], draw[-1]
                tie_breaker = aux.remove_duplicates(current_part[start:end+1])
                current_part[start:end+1] = tie_breaker


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
