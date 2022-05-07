'''
Escribir una programa que permita ingresar un texto y un caracter e imprima la palabra
más larga en la que se encuentra ese carácter.
'''

cadena = input("Ingrese el texto: ")
caracter = input("Ingrese el caracter: ")
cadena_larga = ""

# Convierto el texto en una lista separando los elementos por espacios
lista = cadena.split()

# Recorro la lista
for palabra in lista:
    # Compruebo si la letra está en la palabra, y que además sea la más larga con esa letra
    if caracter in palabra and len(palabra) > len(cadena_larga):
        cadena_larga = palabra # Reemplazo la nueva palabra encontrada por la última guardada

print(f"La palabra más larga en la que se encuentra la letra '{caracter}' es: {cadena_larga}")
