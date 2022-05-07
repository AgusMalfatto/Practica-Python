'''
Las palabras panvocálicas son las que tienen las cinco vocales. Por ejemplo: centrifugado,
bisabuelo, hipotenusa. Escriba la función esPanvocalica(palabra) que indique si una
palabra es panvocálica o no:
esPanvocalica('educativo') ---> True
esPanvocalica('pedagogico') ---> False
'''

# Función que define si la palabra es panvólica o no
def Es_Panvolica(palabra, lista):
    control = "Es panvólica"
    palabra = palabra.lower()
    # Recorro la lista de vocales
    for vocal in lista:
        if not(vocal in palabra): # Si al menos una vocal no está en la palabra entonces no es panvólica
            control = "No es panvólica"
            break
    return control

cadena = input("Ingrese la cadena: ")
lista = ['a', 'e', 'i', 'o', 'u']

# Llamo a la función y le envío la palabra y la lista de vocales
panvolica = Es_Panvolica(cadena, lista)

print(panvolica)