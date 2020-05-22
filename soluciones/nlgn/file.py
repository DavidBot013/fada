import random

animales = []
grandeza = []
apertura = []
partes = []
grande = 0

n = int(input("cantidad de animales: "))
m = int(input("cantidad de partes: "))
while m > 60:
    m = int(input("cantidad de partes: "))
k = int(input("cantidad de escenas: "))
while k > n:
    k = int(input("cantidad de escenarios en cada parte "))

for i in range(n):
    animal = input("ingresar animal: ")
    
    while animal in animales:
        print('ya existente')
        animal = input("ingresar animal: ")
    
    grande = int(input("su grandeza: "))
    while grande in grandeza:
        print('ya existe un animal con esa grandeza')
        grande = int(input("ingrese la grandeza del animal "))

    animales.append(animal)
    grandeza.append(grande)

for i in range((m-1)*k):
    apertura.append([])
    for j in range(3):
        select = animales[random.randrange(n)]
        while select in apertura[i]:
                select = animales[random.randrange(n)]
        apertura[i].append(select)

archivo = open('entrada.txt', 'w') 
archivo.write('n = '+str(n)+'\n')
archivo.write('m = '+str(m)+'\n') 
archivo.write('k = '+str(k)+'\n')
archivo.write('animales = '+str(animales)+'\n')
archivo.write('grandeza = '+str(grandeza)+'\n\n')
archivo.write('apertura = '+str(apertura)+'\n\n')
for i in range(m-1):
    for p in range(k):
        select = apertura[random.randrange(len(apertura))]
        while select in partes:
            select = apertura[random.randrange(len(apertura))]
        partes.append(select)
    archivo.write('parte = '+str(partes)+'\n')
    partes.clear() 
  
archivo.close() 