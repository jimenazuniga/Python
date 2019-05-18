# -*- coding: utf-8 -*-

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    # Área de un círculo
    def area_circulo(self):
        pi = 3.14159
        return pi*(self.radio**2)


circulo = Circulo(8)
print("El área del círculo es ", circulo.area_circulo())
