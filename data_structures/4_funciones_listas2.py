# -*- coding: utf-8 -*-

# ------------- Funciones en listas -------------
lista_alfa = [0, 1, 10, [3, 4]]
# Uso de index en listas
print (lista_alfa.index(10))
print (lista_alfa[3].index(3))
#print (lista_alfa[3].index(1)) #Error por indice

if 12 in lista_alfa:
    print ("Find")
else:
    print ("Not Find")

# Uso de in en listas
print (2 in lista_alfa)
print (3 in lista_alfa)
print (3 in lista_alfa[3])

#Uso de not in en listas
print (2 not in lista_alfa)
print (3 not in lista_alfa)
print (3 not in lista_alfa[3])
print (not 3 in lista_alfa[3])
