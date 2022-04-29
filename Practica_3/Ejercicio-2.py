'''
Una palabra es "alfabética" si todas sus letras están ordenadas alfabéticamente. Por
ejemplo, "amor", "chino" e "himno" son palabras "alfabéticas". Diseña un programa que lea
una palabra y nos diga si es alfabética o no.
'''

from ntpath import join
palabra = input("Ingrese una palabra: ")

# Creo una nueva palabra producto de ordenar alfabéticamente el string ingresado por el usuario
nueva_palabra = ''.join(sorted(palabra)) # 'sorted' ordena el string y devuelve una lista -- ''.join convierte la lista en string

# Comparo que ambas palabras sean iguales
valor = palabra == nueva_palabra

if valor:
    mensaje = "La palabra es alfabética"
else:
    mensaje = "La palabra no es alfabética"

print(mensaje)
