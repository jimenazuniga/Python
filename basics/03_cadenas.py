# -*- coding: utf-8 -*-

# --------------- Uso de cadenas ---------------

# Cuando se imprime una palabra sin comillas Python
# la interpreta como una variable, si ésta no existe
# se arroja un error en tiempo de ejecución
#print (Hola)

# Las cadenas se pueden crear con comillas simples
# o con comillas dobles
print ('Curso')
print (" de Python\n")

# --------------- Cadenas y números ---------------
nombre = "Marco"
print ("Hola " + nombre + "! \n")

num_tortugas = 2

# Los números se deben convertir a cadenas o
# se arrojará un error
#print (nombre + " tiene " + num_tortugas + " tortugas \n")

# Los números se convierten a cadena a través
# de la función str()
print (nombre + " tiene " + str(num_tortugas) + " tortugas \n")

