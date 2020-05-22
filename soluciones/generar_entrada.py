#!/usr/bin/env python3
import sys
import random
import itertools

n = int(sys.argv[1])
m = int(sys.argv[2])
k = int(sys.argv[3])

ANIMALES = []
GRANDEZAS = []
OPENING = []
PARTS = []

for i in range(n):
    animal = input("Ingresar animal: ")

    while animal in ANIMALES:
        print('Ya existe,', end=' ')
        animal = input("ingresar un animal distinto")
    
    greatness = input("Inserte la grandeza del animal: ")
    while greatness in GRANDEZAS:
        print('Todas las grandezas deben ser distintas, ', end=' ')
        greatness = input("inserte la grandeza del animal")

    ANIMALES.append(animal)
    GRANDEZAS.append(greatness)

for i in range((m-1)*k):
    while True:
        scene = random.sample(ANIMALES, 3)
        scene_2 = [scene[2], scene[1], scene[0]]
        scene_3 = [scene[1], scene[0], scene[2]]
        scene_4 = [scene[0], scene[2], scene[1]]
        scene_5 = [scene[2], scene[0], scene[1]]
        scene_6 = [scene[1], scene[2], scene[0]]
        if (scene not in OPENING or 
                scene_2 not in OPENING or 
                scene_3 not in OPENING or 
                scene_4 not in OPENING or
                scene_5 not in OPENING or
                scene_6 not in OPENING):
            break
        
    OPENING.append(scene)

count = [0]*len(OPENING)

while 0 in count:
    for i in range(m-1):
        part = []
        for j in range(k):
            _scene = random.choice(OPENING)
            while _scene in part:
                _scene = random.choice(OPENING)
            
            count[OPENING.index(_scene)] += 1
            part.append(_scene)

        PARTS.append(part)

with open("problem.txt", "w") as file:
    file.write(str(n) +'\n')
    file.write(str(m) +'\n')
    file.write(str(k) +'\n')
    file.write(str(ANIMALES)+'\n')
    file.write(str(GRANDEZAS)+'\n')
    file.write(str(OPENING)+'\n')
    for part in PARTS:
        file.write(str(part) + '\n')
