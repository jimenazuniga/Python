# -*- coding: utf-8 -*-

# Ciclo for
lista = [3, 4, 5, 6]
for elemento in lista:
    print (elemento)

# La función range ayuda a generar un rango de números
lista1 = []
lista2 = []
lista3 = []
lista4 = []


for elemento in range(5, 10): #limite abierto n-1
    lista1.append(elemento)
print (lista1)
for elemento in range(5): #0...n-1 (0 1 2 3 4)
    lista2.append(elemento)
print (lista2)

listaRange = range(5, 50, 5) #Inicio 5, termino 50-1, incremento de 5
for elemento in listaRange:
    print (elemento)

for elemento in range(5):
    print ("Hola")

for elemento in "programando aqui":
    print (elemento.upper())

print("------------------------")
for i in range(5, 0, -1): #5 4 3 2 1
    lista3.append(i)
print (lista3)


print("------------------------")
for i in range(-6, 7, 2): #-6 -4 -2 0 2 4 6
    print(i)

print("------------------------")
#Range NO permite decimales
for i in range(0, 5): #0 0.1 -0.2 0.3 0.4 0.5 0.6
    print(i/10, end=' | ') #end cambia final de linea, por default es salto de linea

print("\n------------------------")

