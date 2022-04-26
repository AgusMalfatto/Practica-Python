'''
Implementa un programa que muestre todos los múltiplos de 6 entre 6 y 150, ambos
inclusive.
'''

for i in range(6, 151):
    entero = i/6 - i//6
    if entero == 0:
        print(i)