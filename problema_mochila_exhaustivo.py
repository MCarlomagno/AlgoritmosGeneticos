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

def selecciona_conjunto(lista_completa):
    conj_solucion = []
    volumen = 0
    vol_total = 0
    for subcon in lista_completa:
        volumen = calcula_volumen(subcon[0])
        if(vol_total<= VOL_MOCHILA and volumen<=VOL_MOCHILA):
            vol_total += volumen
            conj_solucion = subcon[0]
            break

    return conj_solucion

#-----------------------------------------------------------------------------------

lista = [(1,150,20),(2,325,40),(3,600,50),(4,805,36),(5,430,25),(6,1200,64),(7,770,54),(8,60,18),(9,930,46),(10,353,28)]



combinaciones=[]
todos= []




for a in range(len(lista)):
    combinaciones.append([lista[a]])
    for b in range(a+1,len(lista)):
        combinaciones.append([lista[a] , lista[b]])
        for c in range(b+1,len(lista)):
            combinaciones.append([lista[a] , lista[b] , lista[c]])
            for d in range(c+1,len(lista)):
                combinaciones.append([lista[a] , lista[b], lista[c], lista[d]])
                for e in range(d+1,len(lista)):
                    combinaciones.append([lista[a] , lista[b], lista[c], lista[d], lista[e]])
                    for f in range(e+1,len(lista)):
                        combinaciones.append([lista[a] , lista[b], lista[c], lista[d], lista[e],lista[f]])
                        for g in range(f+1,len(lista)):
                            combinaciones.append([lista[a] , lista[b], lista[c], lista[d], lista[e],lista[f],lista[g]])
                            for h in range(g+1,len(lista)):
                                combinaciones.append([lista[a] , lista[b], lista[c], lista[d], lista[e],lista[f],lista[g],lista[h]])
                                for i in range(h+1,len(lista)):
                                    combinaciones.append([lista[a] , lista[b], lista[c], lista[d], lista[e],lista[f],lista[g],lista[h],lista[i]])
                                    for j in range(i+1,len(lista)):
                                        combinaciones.append([lista[a] , lista[b], lista[c], lista[d], lista[e],lista[f],lista[g],lista[h],lista[i],lista[j]])



lista_con_valor = []

for coleccion in combinaciones:
    lista_auxiliar = []
    precio = calcula_valor(coleccion)
    lista_auxiliar.extend([coleccion,precio])
    lista_con_valor.append(lista_auxiliar)

lista_ordenada = sorted(lista_con_valor,key = lambda colec: colec[1],reverse = True)

conjunto_solucion = []

conjunto_solucion = selecciona_conjunto(lista_ordenada)

print conjunto_solucion

vol_max = calcula_volumen(conjunto_solucion)
prec_max = calcula_valor(conjunto_solucion)


print ("volumen del optimo: " + str(vol_max))
print ("valor del optimo: " + str(prec_max))