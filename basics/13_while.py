# -*- coding: utf-8 -*-

def cuenta(entLimite):
    i = entLimite
    while True: # Ciclo infinito
        print (i)
        i = i - 1
        if i == 0:
            break  # Rompiendo el ciclo


cuenta(10)


def factorial(entNumero):
	i = 2
	tmp = 1
	while i < entNumero + 1:
		tmp = tmp * i
		i = i + 1
	return tmp


print (factorial(4))
print (factorial(5))
print (factorial(6))
