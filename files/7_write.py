# -*- coding: utf-8 -*-

numbers = ['hello', 'world', 'writelist']
print("write()")

with open("file.txt", "w") as file:
    print(file.write("Hello world with write!\n"))
    print(file.writelines(numbers))
    print(file.writelines(numbers))
    
with open("file.txt", "r") as file:
	print(file.readlines())

with open("file.txt", "a+") as file:
    print(file.write("Hello world with write!\n"))
    print(file.writelines(numbers))
    print(file.writelines(numbers))
    
with open("file.txt", "r") as file:
	print(file.readlines())