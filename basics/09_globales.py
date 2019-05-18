# -*- coding: utf-8 -*-

cont = 0


def incrementar():
    global cont
    #cont = 0
    cont += 5


incrementar()
incrementar()
print (cont)
