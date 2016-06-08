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


def selecciona_conjunto(lista_ord):
    peso_total = 0
    conj_solucion = []
    for elem in lista_ord:
        peso_total += elem[0][1]
        if(peso_total < PESO_MAX):
            conj_solucion.append(elem[0])
        else:
            peso_total -= elem[0][1]
    return conj_solucion


#--------------------------------------

lista = [(1,1800,72),(2,600,36),(3,1200,60)]

lista_de_valores = map(lambda tupla: tupla[2]/float(tupla[1]), lista)

lista_con_valor= []

for i in range(3):
    lista_con_valor.append([lista[i],lista_de_valores[i]])

lista_ordenada = sorted(lista_con_valor, key = lambda elemento: elemento[1],reverse = True)

conjunto_solucion = selecciona_conjunto(lista_ordenada)

peso = calcula_peso(conjunto_solucion)

val = calcula_valor(conjunto_solucion)

print(conjunto_solucion)
print ("peso del optimo: "+ str(peso) + ".\nvalor del optimo: " + str(val))
