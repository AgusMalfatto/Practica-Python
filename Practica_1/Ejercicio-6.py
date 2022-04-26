'''
Escribir un programa que permita ingresar tres números enteros y escribirlos en orden
creciente.
'''

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    if num2 >= num3:
        print(f"{num3}, {num2}, {num1}")
    else:
        print(f"{num2}, {num3}, {num1}")
elif num2 > num1 and num2 > num3:
    if num1 >= num3:
        print(f"{num3}, {num1}, {num2}")
    else:
        print(f"{num1}, {num3}, {num2}")
else:
    if num1 > num2:
        print(f"{num2}, {num1}, {num3}")
    else:
        print(f"{num1}, {num2}, {num3}")