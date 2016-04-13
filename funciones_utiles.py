"""""
este modulo tiene funciones que sirven
para hacer programas de AG que usen matrices como
poblaciones y numeros enteros para genes
"""""

def iniciarPoblacion(tam_cromosoma,tam_poblacion,rango_random):

    """""
    recibe los enteros tam_cromosoma y tam_poblacion, tambien
    una lista "rango random" que representa el inicio y fin de la poblacion
    """""

    poblacion = []
    for i in range(ram_poblacion):
        cromosoma = []
        for j in range(tam_cromosoma):
            cromosoma.append(random.randint(rango_random[0],rango_random[1]))
        poblacion.append(cromosoma)
    return poblacion


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
    return nuevo_par