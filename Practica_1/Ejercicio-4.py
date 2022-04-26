'''
Diseña un programa que, dado un número entero, determine si éste es el doble de un
número impar. (Ejemplo: 14 es el doble de 7, que es impar.)
'''

numero = int(input("Ingrese un número: "))
mitad = numero / 2

if mitad%2 == 0:
    print(f"El número {numero} es el doble de {mitad}, el cual es par")
else:
    print(f"El número {numero} es el doble de {mitad}, el cual es impar")
