# -*- coding: utf-8 -*-
import pickle

print("pickle")
memory = ['Hello','world','pickle','!!']
file = open('list.txt', 'wb') #Pickle necesita que se abra en binario
#append agrega lineas al texto sin sobreescribir
pickle.dump(memory, file)
file.close()

file = open('list.txt', 'rb')
file_memory = pickle.load(file)
file.close()

print(file_memory)

