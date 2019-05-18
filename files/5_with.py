# -*- coding: utf-8 -*-
import locale

############## Manejo de archivos ##############

with open("5_with.py", "r", encoding='utf-8') as file: #With permite cerrar el archivo automaticamente cuando se ejecute el bloque
    print(locale.getpreferredencoding())
    # LANG environment variable
    print(locale.setlocale(locale.LC_ALL, ''))

