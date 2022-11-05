from numpy import mean, median, std

def ordenar_lista(lista_A, lista_B):
    '''La siguiente funcion se encarga de ordenar 
    de menor a mayor la suma de dos listas'''

    lista_total = lista_A + lista_B

    return sorted(lista_total)



def remover_pares(listaA):
    '''Esta funcion se encarga de remover los
    numeros pares de una lista de numeros'''

    pops = 0
    
    for i in range(len(listaA)):
        if listaA[i-pops] % 2 == 0:
            listaA.pop(i-pops)
            pops += 1
    
        

lista1 = [13,2,104,45,36,9,120,29,2,500,89,4165]

lista2 = [203,30,190,47,22,77,0,177,110,313,15,23]

lista3 = lista1


print(ordenar_lista(lista1, lista2),"\n")

#Calculo de la media, mediana y desviacion
media1 = mean(lista1)
media2 = mean(lista2)

mediana1 = median(lista1)
mediana2 = median(lista2)

desviacion1 = std(lista1)
desviacion2 = std(lista2)

print('La media, mediana y desviacion estandar de la lista 1 son: ')
print("- Media: {:0.4f}".format(media1))
print("- Mediana: {:0.4f}".format(mediana1))
print("- Desviacion: {:0.4f}".format(desviacion1))

print('\nLa media, mediana y desviacion estandar de la lista 2 son: ')
print("- Media: {:0.4f}".format(media2))
print("- Mediana: {:0.4f}".format(mediana2))
print("- Desviacion: {:0.4f}".format(desviacion2))



remover_pares(lista3)
print("\nLista 3 (lista 1 sin pares):\n", lista3)

