# -*- coding: utf-8 -*-
import sys

############## Manejo de excepciones ##############
try:
    file_name = "uno.txt"
    fout = open('uno.txt','r')
    print ("Abre archivo", file_name)
    val = fout.readline()
    print("Lee número")
    x = int(val)
    print ("Convierte número a entero")
    print ("Promedio " + str(101. / x))
    fout.close()
except IOError:
    print ("Error E/S")
except ValueError:
    print ("No pude convertir el dato a un entero.")
except:
    print ("Error inesperado:", sys.exc_info()[0])

print ("Continúa la ejecución del programa fuera del bloque try-catch.")
