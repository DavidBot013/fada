#!/usr/bin/env python3
import pprint, sys
import sys, json
import lineal

file = sys.argv[1]
# Se encarga de "traducir" cada línea del archivo entrada
# a tipos de datos trabajables.
def process_input(file):
    with open(file) as _input:
        lines = _input.readlines()
    
    N,M,K= int(lines[0]), int(lines[1]), int(lines[2]) 

    animals = json.loads(lines[3])
    greatness = json.loads(lines[4])
    animals_dict = dict(zip(animals, greatness)) # Diccionario (animal:grandeza) O(N)

    parts = [json.loads(lines[i]) for i in range(5, (M-1)+6)]
    lineal.sort_rest_of_scenes(parts, N, animals_dict) 
    lineal.sort_parts(parts, animals_dict)
    write_solution(parts)

def write_solution(parts):
    for i in range(len(parts)):
        if i == 0:
            print('Apertura: ', end=' ')
            pprint.pprint(parts[0])
        else:
            print('Parte: ', end=' ')
            pprint.pprint(parts[i])

process_input(file)
