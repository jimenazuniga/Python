# -*- coding: utf-8 -*-
import locale

############## Manejo de archivos ##############
file = None
try:
    file = open("2_open.py", "r", encoding='utf-8')
    print(locale.getpreferredencoding()) #Codificacion de preferencia
    print(locale.setlocale(locale.LC_ALL, '')) #Localizacion regional
except:
    print('No fue posible abrir el archivo.')

finally:
    print("Dento de finally")
    if file:
        file.close
