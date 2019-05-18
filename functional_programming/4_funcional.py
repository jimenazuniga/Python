# -*- coding: utf-8 -*-

# Área de un círculo
pi = 3.14159
area_circulo = lambda entRadio:pi*(entRadio**2)
radio = 8

# 1ra forma
print("El área del círculo es", area_circulo(radio))
# 2da forma
print("El área del círculo es",(lambda entRadio:pi*(entRadio**2))(radio))
