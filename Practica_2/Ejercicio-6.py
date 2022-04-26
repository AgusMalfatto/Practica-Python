'''
Diseñar un programa que genere una lista de números usando el siguiente proceso:
comenzar con un entero n que deberá ingresar el usuario. Si n es par, dividirlo por 2. Si n
es impar, multiplicarlo por 3 y sumarle 1. Repetir este proceso hasta que el nuevo valor
obtenido para n sea 1.
Ejemplo, para n = 22, la secuencia que se obtiene es:
22 11 33 17 52 26 13 40 20 10 5 16 8 4 2 1
'''

num = int(input("Ingrese un número: "))
while num <= 0:
    num = int(input("Error, ingrese un número positivo: "))
lista = [num]
while num != 1:
    if num%2 == 0:
        num //= 2
        lista.append(num)
    else:
        num = num * 3 + 1
        lista.append(num)

print(lista)