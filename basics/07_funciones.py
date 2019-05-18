# -*- coding: utf-8 -*-
# ------------- Definición de funciones -------------


def imprimeNombre(cadNombre):
    print (cadNombre)
    return cadNombre[0], cadNombre[-1]


def quienEs(cadNombre):
    print (cadNombre + " mejor conocido como el Zorro.\n")


# ------------- Llamada a funciones -------------
cadena = "Alejandro Murrieta"
[x, y] = imprimeNombre(cadena)

# Se imprimen los valores que regresa la función imprimeNombre
print (x)
print (y)
quienEs(cadena)


def segunda_coincidencia(cadUno, cadDos):
    first = cadUno.find(cadDos)
    return cadUno.find(cadDos, first + 1)


s1 = "Amor y deseo son dos cosas diferentes; que no todo lo que se ama se desea, ni todo lo que se desea se ama. (Don Quijote)"
s2 = "ama"

print (segunda_coincidencia(s1, s2))
