'''
Diseña un programa que solicite la lectura de un número entre 0 y 10 (ambos inclusive).
Si el usuario teclea un número fuera del rango válido, el programa solicitará nuevamente
la introducción del valor cuantas veces sea menester.
'''

num = int(input("Ingrese un número: "))

while num < 0 or num > 10:
    num = int(input("Error, ingrese un número entre '0' y '10': "))

print("Número correcto")