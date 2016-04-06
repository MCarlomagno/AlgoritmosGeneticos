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
COEF = 2 ** 30 - 1

import random
import matplotlib.pyplot as plt


def iniciarPoblacion():

    """""
    La poblacion constara de 10 cromosomas,
    cada uno de ellos compuestos de 30 genes binarios
    que representan los decimales correspondientes al dominio [0,2**30-1]
    """""

    poblacion = []
    for i in range(0, 10):
        cromosoma = []
        for j in range(0, 30):
            cromosoma.append(random.randint(0, 1))
        poblacion.append(cromosoma)
    return poblacion


def pasa_a_decimal(cromo):

    """""
    recibe una lista de binarios, retorna el valor decimal que le corresponde
    """""

    valor_entero = 0
    j = 0
    for i in range(len(cromo)-1, -1, -1):
        valor_entero += cromo[i] * 2 ** j
        j += 1
    return valor_entero


def cargaFitness(poblacion):

    """""
    #recibe la poblacion y duevuelve una lista
    de la forma [(cromosoma,fitness),...]
    """""

    suma = 0
    array = []
    for cromosoma in poblacion:
        valor_entero = pasa_a_decimal(cromosoma)
        funcion_obj = (valor_entero / float(COEF)) ** 2
        array.append(funcion_obj)
        suma += funcion_obj

    for cromo in poblacion:
        fitness = array[poblacion.index(cromo)] / float(suma)
        tupla = (cromo, fitness)
        poblacion[poblacion.index(cromo)] = tupla
    return poblacion


def cargaRuleta(pob_fitness):

    """""
    #recibe una lista de tuplas de la forma [(cromosoma,fitness),...]
    y retorna otra lista de tuplas con [(ang_min,ang_max,cromosoma),...]
    """""

    ruleta = []
    ac = 0.0
    for cromo in pob_fitness:
        angulo = cromo[1] * 360
        tupla = (ac, ac + angulo, cromo[0])
        ruleta.append(tupla)
        ac += angulo
    return ruleta


def buscaPadre(numero,ruleta):

    """""
    recibe un numero al azar entre 0 y 360 y devuelve
    el cromosoma que corresponde al intervalo que contiene el numero
    """""

    for rang in ruleta:
        if (numero > rang[0])and(numero <= rang[1]):
            padre = rang[2]
            break
    return padre


def crossOver(par):

    """""
    recibe una lista que contiene el par de padres
    y devuelve una lista con el par de hijos
    """""

    punto_corte = random.randint(1, 29)
    cromo1 = par[0]
    cromo2 = par[1]
    prefijo1 = cromo1[:punto_corte]
    sufijo1 = cromo2[punto_corte:]
    prefijo2 = cromo1[punto_corte:]
    sufijo2 = cromo2[:punto_corte]
    hijo1 = prefijo1 + sufijo1
    hijo2 = prefijo2 + sufijo2
    nuevo_par = [hijo1, hijo2]
    return nuevo_par


def mutacion(cromosoma):

    """""
    recibe un cromosoma(lista de binarios)
    y devuelve el mismo mutado.
    """""

    pos_gen = random.randint(0, 29)
    if cromosoma[pos_gen] == 1:
        cromosoma[pos_gen] = 0
    else:
        cromosoma[pos_gen] = 1
    return cromosoma

def calcula_datos(poblacion):

    """""
    recibe una poblacion (lista de cromosomas) y devuelve
    una tupla que contiene minimo,maximo y promedio de los cromosomas
    """""

    acu = 0
    for cromo in poblacion:
        acu += cromo
    prom = acu / float(len(poblacion))
    maximo = max(poblacion)
    minimo = min(poblacion)
    tup = (minimo, maximo, prom)
    return tup

#programa principal

poblacion = iniciarPoblacion()
lista_de_datos = []
for k in range(500):
    lista_dec = []
    for cromosoma in poblacion:
        valor = pasa_a_decimal(cromosoma)
        lista_dec.append(valor)

    datos = calcula_datos(lista_dec)
    lista_de_datos.append(datos)

    print(("en la poblacion: " + str(k) + " min,max,prom = " + str(datos)))

    pob_fitness = cargaFitness(poblacion)
    ruleta = cargaRuleta(pob_fitness)
    padres = []

    for i in range(10):
        #buscar los 10 padres y agregarlos a una lista de padres
        num = random.randint(1, 1000)  # para darle dos decimales
        seleccion = (num / 1000.0) * 360
        pa = buscaPadre(seleccion, ruleta)
        padres.append(pa)

    poblacion = []
    acum = 0

    for j in range(5):
        par = []
        par.extend(padres[acum:acum + 2])
        acum += 2
        numero_rand = random.randint(1, 100)
        if numero_rand <= (PROB_CROSS * 100):
            nuevo_par = crossOver(par)
            poblacion.extend(nuevo_par)
        else:
            poblacion.extend(par)

    for cromosoma in poblacion:
        numero_rand2 = random.randint(0, 100)
        if numero_rand2 <= (PROB_MUT * 100):
            poblacion[poblacion.index(cromosoma)] = mutacion(cromosoma)

print("\n\n")
print(poblacion)

plt.plot(lista_de_datos)
plt.ylabel("Verde: maximo\nAzul: minimo\nRojo: promedio")
plt.xlabel("Poblacion")
plt.show()