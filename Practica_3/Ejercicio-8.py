'''
Ejercicio 8:
Un ISBN-10 (International Standard Book Number) consiste de 10 dígitos:
d1d2d3d4d5d6d7d8d9d10.
El último dígito, d10, es el dígito verificador que se calcula como sigue:
Si el dígito verificador es 10, el último dígito es x, de acuerdo a las normas ISBN. Escribir
un programa que permita ingresar los primeros 9 dígitos como una cadena y muestre el
número ISBN.
Ejemplo: 013601267 ---> 0136012671
 013031997 ---> 013601267X

'''

cadena = input("Ingresar la cadena de números: ")
numero, control = 0, 1
lista_cadena = list(cadena)

# Itero cada dígito ingresado
for i in lista_cadena:
    # Multiplico al dígito por la posición que ocupa
    numero += int(i) * control
    control += 1

numero = numero % 11

# Analizo el resto
if numero == 10:
    lista_cadena.append('X')
else:
    lista_cadena.append(numero)

# Imprimo en número resultante
for i in lista_cadena:
    print(int(i), end="")