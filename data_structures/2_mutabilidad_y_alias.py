# -*- coding: utf-8 -*-

# ------------- Mutacion y referencias -------------

c1 = 'Hola'
c2 = c1        # Otra referencia a la cadena

print (c1)
print (c2)

print (c2[1])

#c1[0] = 'B'    # operacion no permitida
#c1[0] = c2    # operacion no permitida
c1 = 'Bola'    # Nueva cadena creada

# Al imprimir las cadenas, ya no son iguales, no apuntan a la misma información
print (c1)
print (c2)

# ------------- Listas -------------
lista = ['H', 'o', 'l', 'a']
lista2 = lista     # Otra referencia a la lista
print (lista)

lista[0] = 'B'
lista2[0] = 'Y'
# Al imprimir las listas, las dos referencias apuntan a la misma informacion
print (lista)
print (lista2)


def mutarLista(lista):
    lista[3] = 'G'


mutarLista(lista)
print (lista)
