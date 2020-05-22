from time import time
import sys
#Métodos utilizados para ordenamiento

def escenas(A,down,high): 
    global conteo
    global output
    conteo = [zoo[A[i]] for i in range(3)]

    if zoo.get(A[down]) < zoo.get(A[high]):
        min = zoo.get(A[down])
        max = zoo.get(A[high])
        
    else:
        max = zoo.get(A[down])
        min= zoo.get(A[high])
        A[down],A[high] = A[high],A[down]

    for j in range(down+1, high):
        if  zoo.get(A[j]) >= max: 
            A[j],A[high] = A[high],A[j]
        else:
            if zoo.get(A[j]) <= min:
                A[j],A[down] = A[down],A[j]
    
    for i in range(len(conteo)):
        output[conteo[i]-1]+=1 


def GrandMaximaEscena(size,A):
    global escenaMax
    if size > escenaMax:
        escenaMax = size
        arrayEscMax.clear()
        arrayEscMax.append(A)

def GrandMinimaEscena(size,A):
    global escenaMin
    if escenaMin == 0:
        escenaMin = size
        arrayEscMin.append(A)

    if escenaMin > size:
        escenaMin = size
        arrayEscMin.clear()
        arrayEscMin.append(A)

def sizeScene(A):
    size = 0
    global media
    global k
    try:
        for j in range(0,2):    
            size +=zoo.get(A[j])
        GrandMaximaEscena(size,A)
        GrandMinimaEscena(size,A)

    except:
        for p in range(len(A)):
            for j in range(0,2):
                size +=zoo.get(A[p][j])
            GrandMaximaEscena(size,A[p])
            GrandMinimaEscena(size,A[p])
            size = 0
    
    return size

def mergeSort(A): 
    if len(A) >1: 
        mid = len(A)//2  
        L = A[:mid] 
        R = A[mid:] 
        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if sizeScene(L[i]) < sizeScene(R[j]): 
                A[k] = L[i] 
                i+=1
            else: 
                if sizeScene(L[i]) == sizeScene(R[j]):
                    if L[i][2] < R[i][2]:
                        A[k] = L[i] 
                        i+=1
                    else:
                        A[k] = R[j] 
                        j+=1
                else:
                    A[k] = R[j] 
                    j+=1
            k+=1
          
        while i < len(L): 
            A[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            A[k] = R[j] 
            j+=1
            k+=1

#Métodos utilizados para sacar los reportes

def PromedioApertura(A):
    size = 0
    global media
    for j in range(0,3):
        size +=zoo.get(A[j])
    media = media + size

def menosParticipante(A):
    min = A[0]
    arreglo = []
    j = 0
    for i in range(1,len(A)):
        if min > A[i]:
            min = A[i]
            arreglo.clear()
            arreglo.append(i)
        else:
            if min == A[i]:
                arreglo.append(i)

    print("Animales menos participantes: ")
    
    for i in range(len(arreglo)):
        print(str(grand.get(arreglo[i]+1)))
    
    print(" en "+str(min)+" escenarios." )

def masParticipante(A):
    max = A[0]
    arreglo = []
    j = 0
    for i in range(1,len(A)):
        if max < A[i]:
            max = A[i]
            arreglo.clear
            arreglo.append(i)
        else:
            if max == A[i]:
                arreglo.append(i)
    print("Animales más participantes: ")
    
    for i in range(len(arreglo)):
        print(str(grand.get(arreglo[i]+1)))
    
    print(" en "+str(max)+" escenarios. " )


#Método principal, lee el archivo, llena las estructuras de datos y llama los métodos.

if __name__ == '__main__': 
    lista = []
    apertura = []
    partes = []
    x=0
    y=3

    arrayEscMax = []
    arrayEscMin = []
    
    escenaMax = 0
    escenaMin = 0

    media = 0

    archivo = open(sys.argv[1], 'r')
    
    with open(sys.argv[1], 'r') as procfile:
        for line in procfile:
            if line.split() != []:
                lista.append(line.replace(';','').replace('{','[').replace('}',']').replace("'",'').split()[2:])

    n = int(lista[0][0])
    m = int(lista[1][0])
    k = int(lista[2][0])

    conteo = [0 for _ in range(n)]
    output = [0] * n


    animales = [lista[3][i].replace('[','').replace(',','').replace(']','') for i in range(n)]
    grandezas = [int(lista[4][i].replace('[','').replace(',','').replace(']','')) for i in range(n)]

    for g in range((m-1)*k):
        apertura.append([])
        for i in range(x,y):
            apertura[g].append((lista[5][i].replace('[','').replace(',','').replace(']','')))
        x +=3
        y +=3

    x = 0
    y = 3

    for r in range(m-1):
        partes.append([])
        for t in range(k):
            partes[r].append([])
            for i in range(x,y):
                partes[r][t].append((lista[6+r][i].replace('[','').replace(',','').replace(']','')))
            x += 3
            y += 3
        x = 0
        y = 3

   
    zoo= dict(zip(animales,grandezas))
    grand = dict(zip(grandezas,animales))

    tinicial = time()
    
    for i in range((m-1)*k):
        escenas(apertura[i],0,2)

    for i in range(m-1):
        for j in range(0,k):
            escenas(partes[i][j],0,2)
    
    mergeSort(apertura)
  
    for i in range((m-1)*k):
            PromedioApertura(apertura[i])
    
    media = media/((m-1)*k)

    for i in range(m-1):
        mergeSort(partes[i])

    mergeSort(partes)
    print('El orden de presentacion es: \n')
    print('Apertura: ' + str(apertura))

    for i in range(0,m-1):
        print('Parte '+str(i+1)+ str(partes[i])+": ")
    
    menosParticipante(output)
    masParticipante(output)

    print('La escena con mayor grandeza fue: '+ str(arrayEscMax))
    print('La escena con menor grandeza fue: '+ str(arrayEscMin))
    print('La media de grandeza: '+ str(media))

tfinal = time()
tejecucion = tfinal - tinicial
print ('El tiempo de ejecucion fue:',tejecucion) 
