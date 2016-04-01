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
PROB_CROSS = 0.75
PROB_MUT = 0.05

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
        j = 0
        for i in range(len(cromosoma)-1,-1,-1):
            valor_entero += cromosoma[i]*2**j
            j+=1
        cromosoma.append(valor_entero) #asigno el entero como un ultimo elemento de la lista
        suma += valor_entero
    #en este bucle calculo el fitness de cada cromosoma y lo cargo a la poblacion
    for cromo in poblacion:
        fitness = cromo[30]/float(suma)
        cromo.pop(30)
        tupla = (cromo,fitness)
        poblacion[poblacion.index(cromo)] = tupla
    return poblacion

def cargaRuleta(pob):
    """""
    para armar la ruleta hacemos una lista de tuplas que le
    corresponde a cada cromosoma con 3 valores, el inicio del arco
    de circunferencia, el fin y el cromosoma
    """""
    ruleta = []
    ac = 0.0
    for cromo in pob:
        angulo = cromo[1]*360
        tupla = (ac,ac+angulo,cromo[0])
        ruleta.append(tupla)
        ac += angulo
    return ruleta

def buscaPadre(numero,ruleta):
    # recibe un numero al azar entre 0 y 360 y devuelve el cromosoma que corresponde al intervalo que contiene el numero
    for rang in ruleta:
        if (numero > rang[0])and(numero <= rang[1]):
            padre = rang[2]
            break
    return padre

def crossOver(par):
    #recibe una lista que contiene el par de padres y devuelve una lista con el par de hijos
    puntoCorte = random.randint(2,30)
    cromo1 = par[0]
    cromo2 = par[1]
    prefijo1 = cromo1[:puntoCorte-1]
    sufijo1 = cromo2[puntoCorte-1:]
    prefijo2 = cromo1[puntoCorte-1:]
    sufijo2 = cromo2[:puntoCorte-1]
    hijo1 = prefijo1 + sufijo1
    hijo2 = prefijo2 + sufijo2
    nuevoPar = [hijo1,hijo2]
    return nuevoPar

def mutacion(cromosoma):
    posgen = random.randint(0,29)
    if cromosoma[posgen] == 1:
        cromosoma[posgen] = 0
    else:
        cromosoma[posgen] = 1
    return cromosoma


#programa principal

poblacion = iniciarPoblacion()
for k in range(0,20):
    pobfitness = cargaFitness(poblacion)
    ruleta = cargaRuleta(pobfitness)
    padres = []
    for i in range(0,10):
        #buscar los 10 padres y agregarlos a una lista de padres
        num = random.randint(1,1000) #para darle dos decimales
        seleccion = (num/1000.0)*360
        padres.append(buscaPadre(seleccion,ruleta))

    acum = 0
    #se toman de a pares de padres para hacer crossover y asignar a la nuevo poblacion
    poblacion = []
    for j in range(0,5):
        par = padres[acum:acum+2]
        acum += 2
        numeroRand = random.randint(1,100)
        if numeroRand <= (PROB_CROSS*100):
            nuevoPar = crossOver(par)
            poblacion.extend(nuevoPar)
        else:
            poblacion.extend(par)

    for cromosoma in poblacion:
        numeroRand2 = random.randint(1,100)
        if numeroRand2 <= (PROB_MUT*100):
            poblacion[poblacion.index(cromosoma)] = mutacion(cromosoma)

print(poblacion)





