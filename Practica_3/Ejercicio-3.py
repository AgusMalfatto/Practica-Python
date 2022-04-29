'''
Hay un tipo de pasatiempos que propone descifrar un texto del que se han suprimido
las vocales. Por ejemplo, el texto ".n .j.mpl. d. p.s.t..mp.s", se descifra sustituyendo cada
punto con una vocal del texto. La solución es "un ejemplo de pasatiempos". Diseña un
programa que ayude al creador de pasatiempos. El programa recibirá una cadena y
mostrará otra en la que cada vocal ha sido reemplazada por un punto.
'''

cadena = input("Ingrese cadena: ")

lista = list(cadena)
lista_aux = ['a', 'e', 'i', 'o', 'u']

# Enumerate permite recorrer la lista con dos variables
for indice, letra in enumerate(lista): #'indice' recorre las posiciones, y 'letra' recorre los valores de la lista
    #si la letra de la cadena se encuentra en la lista de vocales, entonces reemplazo su valor por '.'
    if letra in lista_aux:
        lista[indice] = '.'

# Repongo la cadena en un string
cadena = ''.join(lista)

print(cadena)
