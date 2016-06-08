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
CANT_ELITE = 0

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
    for i in range(len(cromo) - 1, -1, -1):
        valor_entero += cromo[i] * 2 ** j
        j += 1
    return valor_entero


def cargaFitness(poblacion):

    """""
    recibe la poblacion y duevuelve una lista
    de la forma [(cromosoma,fitness),...]
    """""

    suma = 0
    pobla_fitness = []
    funciones_obj = []
    for cromosoma in poblacion:
        valor_entero = pasa_a_decimal(cromosoma)
        funcion_obj = (valor_entero / float(COEF)) ** 2
        funciones_obj.append(funcion_obj)
        suma += funcion_obj

    for cromo in poblacion:
        fitness = funciones_obj[poblacion.index(cromo)] / float(suma)
        tupla = (cromo, fitness)
        pobla_fitness.append(tupla)
    return pobla_fitness


def cargaRuleta(pob_fitness):

    """""
    recibe una lista de tuplas de la forma [(cromosoma,fitness),...]
    y retorna otra lista de tuplas
    con [(inicio_arco_circunf,fin_arco_circunf,cromosoma),...]
    """""

    ruleta = []
    ac = 0.0
    for cromo in pob_fitness:
        angulo = cromo[1] * 360   # en cromo[1] esta el fitness de ese cromosoma
        tupla = (ac, ac + angulo, cromo[0])
        ruleta.append(tupla)
        ac += angulo   # se va incrementando hasta 360.0 (ruleta completa)
    return ruleta


def buscaPadre(numero, ruleta):

    """""
    recibe un numero al azar entre 0 y 360 y devuelve
    el cromosoma que corresponde al intervalo que contiene el numero
    """""

    for rango in ruleta:
        if (numero > rango[0])and(numero <= rango[1]):  # rang[0] y [1] son inicio y fin de arco de circunf.
            padre = rango[2]  # rang[2] contiene el cromosoma asociado al rango
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
    for cromo in nuevo_par:
        cro = pasa_a_decimal(cromo) / float(COEF)
        print("hubo crossover en: " + str(cro))
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
    cro = pasa_a_decimal(cromosoma) / float(COEF)
    print("hubo mutacion en el bit " + str(pos_gen + 1) + " en el cromosoma " +  str(cro))
    return cromosoma

def calcula_datos(poblacion):

    """""
    recibe una poblacion (lista de cromosomas) y devuelve
    una tupla que contiene minimo,maximo y promedio de los cromosomas
    """""

    acu = 0
    for cromo in poblacion:
        acu += cromo
    prom = (acu / float(len(poblacion))) / float(COEF)
    maximo = max(poblacion) / float(COEF)
    minimo = min(poblacion) / float(COEF)
    tup = (minimo, maximo, prom)
    return tup


def mostrarPoblacion(poblacion):

    for cromo in poblacion:
        cromo_dec = pasa_a_decimal(cromo)
        cromo_div = cromo_dec/float(COEF)
        print(cromo_div)

def elite(poblacion_fit):

    '''''
    recibe la poblacion con fitness y retorna los n
    cromosomas(lista de bits) que pasan a la porxima poblacion como elite
    '''''

    lista_fitness = []
    for i in poblacion_fit:
        lista_fitness.append(i[1])
    elites = []
    for j in range(CANT_ELITE):
        maximo = max(lista_fitness)
        indice_max = lista_fitness.index(maximo)
        elites.append(poblacion_fit[indice_max])
        lista_fitness.remove(lista_fitness[indice_max])
    return elites



#programa principal

poblacion = iniciarPoblacion()
mostrarPoblacion(poblacion)
lista_de_datos = []
for k in range(20):
    lista_dec = []
    for cromosoma in poblacion:
        valor = pasa_a_decimal(cromosoma)
        lista_dec.append(valor)

    datos = calcula_datos(lista_dec)
    lista_de_datos.append(datos)

    print(("en la poblacion: " + str(k) + " minimo, maximo, promedio (valor_decimal/coeficiente) = " + str(datos)))

    pob_fitness = cargaFitness(poblacion)
    ruleta = cargaRuleta(pob_fitness)

    padres = []
    for i in range(10):
        num = random.randint(1,1000)
        seleccion = (num / 1000.0) * 360  # seleccion es un flotante de dos decimales entre 0 y 360
        pa = buscaPadre(seleccion, ruleta)
        padres.append(pa)


    tuplas_elites = elite(pob_fitness)
    padres_elites = []
    for tup in tuplas_elites:
        padres_elites.append(tup[0])
    poblacion = []
    poblacion.extend(padres_elites)
    acum = CANT_ELITE
    cont = 0
    for j in range(0,5):
        par = []
        par.extend(padres[acum:acum + 2])
        acum += 2
        nuevo_par = []
        numero_rand = float(random.randint(1, 100))
        if numero_rand <= (PROB_CROSS * 100):
            nuevo_par = crossOver(par)
            poblacion.extend(nuevo_par)
            cont += 1
        else:
            poblacion.extend(par)

    for cromosoma in poblacion:
        numero_rand2 = float(random.randint(0, 100))
        if numero_rand2 <= (PROB_MUT * 100):
            poblacion[poblacion.index(cromosoma)] = mutacion(cromosoma)

plt.plot(lista_de_datos)
plt.ylabel("Verde: maximo\nAzul: minimo\nRojo: promedio")
plt.xlabel("ciclos")
plt.show()