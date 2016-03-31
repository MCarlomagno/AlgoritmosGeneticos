"""""
funcion a maximizar f(x)=(x/coef)**2
dom f = [0,2**30-1]
coef = 2**30-1
probabilidad de crossover = 0,75
probabilidad de mutacion = 0,05
poblacion inicial = 10
ciclos = 20
metodo de seleccion = ruleta
metodo de crossover = 1 punto
metodo de mutacion = invertida
"""""

import random

def iniciarPoblacion():
    """"" La poblacion constara de 10 cromosomas,
    cada uno de ellos compuestos de 30 genes binarios
    que representan los decimales correspondientes al dominio [0,2**30-1]
    """""
    poblacion = []
    for i in range(0,10):
        cromosoma = []
        for j in range(0,30):
            cromosoma.append(random.randint(0,1))
        poblacion.append(cromosoma)
    return poblacion

def cargaFitness(poblacion):
    """""esta funcion recorre la poblacion y, pasando los cromosomas a enteros,
    calcula la suma total y luego el fitness, el cromosoma sera devuelto a la
    poblacion en forma de tupla como: (cromosoma,fitness)
    """""
    #este bucle sirve para calcular la suma de todos los cromosomas
    suma = 0
    for cromosoma in poblacion:
        #bucle feo
        valor_entero = 0
        for i in range(len(cromosoma)-1,-1,-1):
            if (cromosoma[i]==1):
                valor_entero += 2**i
        cromosoma.append(valor_entero) #asigno el entero como un ultimo elemento de la lista
        suma += valor_entero
    #en este bucle calculo el fitness de cada cromosoma y lo cargo a la poblacion
    for cromo in poblacion:
        fitness = cromo[30]/float(suma)
        tupla = (cromo,fitness)
        poblacion[poblacion.index(cromo)] = tupla
        cromo.pop(30)
    return poblacion


#programa principal

poblacion = iniciarPoblacion()
pobfitness = cargaFitness(poblacion)

