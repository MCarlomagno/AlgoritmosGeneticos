""""" encontrar subconjunto de la lista para el cual, el valor $ sea maximo y
sea menor a 3000 gr.
tupla[0] = nro elemento
tupla[1] = peso
tupla[2] = $

 """""


PESO_MAX = 3000

def calcula_valor(lista_elementos):

    acum = 0
    for elem in lista_elementos:
        acum += elem[2]
    return acum


def calcula_peso(lista_elementos):
    """""
    recibe lista de elementos y retorna un
    entero que representa la sumatoria de los mismos
    """""
    acum = 0
    for elemento in lista_elementos:
        acum += elemento[1]
    return acum


def selecciona_conjunto(lista_completa):
    conj_solucion = []
    peso = 0
    peso_total = 0
    for subcon in lista_completa:
        peso = calcula_peso(subcon[0])
        if(peso_total<= PESO_MAX and peso<= PESO_MAX):
            peso_total += peso
            conj_solucion = subcon[0]
            break

    return conj_solucion

#--------------------------------------

lista = [(1,1800,72),(2,600,36),(3,1200,60)]


combinaciones=[]
todos= []

for a in range(len(lista)):
    combinaciones.append([lista[a]])
    for b in range(a+1,len(lista)):
        combinaciones.append([lista[a] , lista[b]])
        for c in range(b+1,len(lista)):
            combinaciones.append([lista[a] , lista[b] , lista[c]])

lista_con_valor = []

for coleccion in combinaciones:
    lista_auxiliar = []
    precio = calcula_valor(coleccion)
    lista_auxiliar.extend([coleccion,precio])
    lista_con_valor.append(lista_auxiliar)

lista_ordenada = sorted(lista_con_valor,key = lambda colec: colec[1],reverse = True)


conjunto_solucion = selecciona_conjunto(lista_ordenada)


print conjunto_solucion

pe_max = calcula_peso(conjunto_solucion)
prec_max = calcula_valor(conjunto_solucion)


print ("peso del optimo: " + str(pe_max))
print ("valor del optimo: " + str(prec_max))