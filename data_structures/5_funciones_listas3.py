
# -*- coding: utf-8 -*-
# ------------- Funciones en listas -------------
#Pop y push en listas
listaA = [1, 2, 3, 4]
print (listaA)
listaA.pop()
listaA.pop(0) #Elimina primer elemento
print ("POP", listaA.pop(0))
print (listaA)

#La función del sirve para eliminar elementos de una lista
listaB = [3, 4, 5, 6]
print (listaB)
del(listaB[2])
print ("DEL [2]")
print (listaB)

#Insertando elementos en la lista
print ("INSERT 5")
listaB.insert(3, 5)
print ("INSERT 15")
listaB.insert(4, 15)
print (listaB)
listaB.insert(0, 15)
print (listaB)
