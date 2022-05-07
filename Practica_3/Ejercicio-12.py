'''
Escribe un programa que lea dos cadenas y devuelva el prefijo común más largo de
ambas. Ejemplo: las cadenas "politécnico" y "polinización" tienen como prefijo común más
largo a la cadena "poli".
'''

cadena_uno = input("Ingrese la primer palabra: ")
cadena_dos = input("Ingrese la segunda palabra: ")
nueva_cadena = ""

# Recorro las cadenas simultáneamente
for letra1, letra2 in zip(cadena_uno, cadena_dos):
    # Comparo las letras
    if letra1 == letra2:
        nueva_cadena += letra1 # Uno la letra al prefijo
    else:
        break

print(f"El prefijo en común es: {nueva_cadena}")

'''
for letra, letra2 in zip(cadena_uno, cadena_dos):
    if letra != letra2:
        break
    lista.append(letra)


lista = ''.join(lista)
'''