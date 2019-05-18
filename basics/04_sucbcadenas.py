# -*- coding: utf-8 -*-

# ------------- Cadenas y subcadenas -------------

# Cadena con 22 caracteres
cadena = "parangaricutirimicuaro"

print (cadena[0])    # Se obtiene el primer carácter
print (cadena[21])   # Se obtiene el último carácter

# Si se pone un indice negativo, la cuenta
# empieza en el �ltimo elemento de la cadena
print (cadena[-2])   # último carácter

# Si se quiere acceder a un elemento fuera de rango
# de la cadena, se obtiene el error
# IndexError: string index out of range
#print (cadena[22])   # Carácter fuera de rango

print (cadena[5:13])  # imprime garicuti
print (cadena[5:])    # imprime garicutirimicuaro
print (cadena[:5])    # imprime param
print (cadena[:])     # imprime la cadena completa
