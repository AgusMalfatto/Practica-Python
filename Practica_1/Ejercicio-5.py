'''
Escribir un programa que permita ingresar dos números enteros y escribirlos en orden
creciente.
'''

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 >= num2:
    print(f"{num2}, {num1}")
else:
    print(f"{num1}, {num2}")
    
