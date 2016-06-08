""""" encontrar subconjunto de la lista para el cual, el valor $ sea maximo y entre en la mochi
tupla[0] = nro elemento
tupla[1] = volumen
tupla[2] = $

 """""

VOL_MOCHILA = 4200

def calcula_valor(lista_elementos):

    acum = 0
    for elem in lista_elementos:
        acum += elem[2]
    return acum

def calcula_volumen(lista_elementos):
    """""
    recibe lista de elementos y retorna un
    entero que representa la sumatoria de los mismos
    """""
    acum = 0
    for elemento in lista_elementos:
        acum += elemento[1]
    return acum

def selecciona_conjunto(lista_ord):
    vol_total = 0
    conj_solucion = []
    for elem in lista_ord:
        vol_total += elem[0][1]
        if(vol_total <= VOL_MOCHILA):
            conj_solucion.append(elem[0])
        else:
            vol_total -= elem[0][1]
    return conj_solucion
#-----------------------------------------------------------------------------------

lista = [(1,150,20),(2,325,40),(3,600,50),(4,805,36),(5,430,25),(6,1200,64),(7,770,54),(8,60,18),(9,930,46),(10,353,28)]


lista_de_valores = map(lambda tupla: tupla[2]/float(tupla[1]), lista)

lista_con_valor= []

for i in range(10):
    lista_con_valor.append([lista[i],lista_de_valores[i]])

lista_ordenada = sorted(lista_con_valor, key = lambda elemento: elemento[1],reverse = True)

conjunto_solucion = selecciona_conjunto(lista_ordenada)

vol = calcula_volumen(conjunto_solucion)

val = calcula_valor(conjunto_solucion)

print(conjunto_solucion)
print ("volumen del optimo: "+ str(vol) + ".\nvalor del optimo: " + str(val))
