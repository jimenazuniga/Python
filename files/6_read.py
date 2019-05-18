# -*- coding: utf-8 -*-
import locale

print("read()")
with open("6_read.py", "r", encoding='utf-8') as file:
    print(file.read())

'''
Bloque Comentarios 

'''
print("\nread(-111)")
with open("6_read.py", "r", encoding='utf-8') as file:
    print(file.read(-111))

print("\nread(10)")
with open("6_read.py", "r", encoding='utf-8') as file:
    print(file.read(10))  #Lee los primeros 10 caracteres, en caso de abrir en modo binario lee los primeros 10 bytes

print("\nread(10) binary")
with open("6_read.py", "rb") as file: # 8 bits = 1 byte
    print(file.read(10))

with open("6_read.py", "r") as file:
    while True:
        line = file.readline()
        if not line: #Rompe el ciclo si la linea es vacia
            break
        print (line)
