'''
Diseña un programa que, dado un número entero, muestre por pantalla el mensaje "El
número es par." cuando el número sea par y el mensaje "El número es impar." cuando sea
impar. (Una pista: un número es par si el resto de dividirlo por 2 es 0, e impar en caso
contrario.)
'''

numero = int(input("Ingrese un número: "))

if numero == 0:
    print("El número es 'cero'.")
elif numero%2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")