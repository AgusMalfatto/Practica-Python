'''
Dos palabras son anagramas si tienen las mismas letras pero en otro orden. Por ejemplo,
«torpes» y «postre» son anagramas, mientras que «aparta» y «raptar» no lo son, ya que
«raptar» tiene una r de más y una a de menos.
Escriba la función sonAnagramas(p1, p2) que indique si las palabras p1 y p2 son
anagramas:
sonAnagramas('torpes', 'postre') ---> True
sonAnagramas('aparta', 'raptar') ---> False
'''

# Función que determina si las palabras son anagramas
def SonAnagramas(palabra1, palabra2):
    control = "Son anagramas"
    # Recorro ambas cadenas
    for letra1, letra2 in zip(palabra1, palabra2):
        # Comparo que las letras sean iguales, si no son iguales -> no son anagramas
        if letra1 != letra2:
            control = "No son anagramas"
    return control

cadena_uno = input("Ingrese la primer palabra: ")
cadena_dos = input("Ingrese la segunda palabra: ")
lista = []

# Ordeno de forma alfabética las dos cadenas
cadena_uno = sorted(cadena_uno)
cadena_dos = sorted(cadena_dos)

# Llamo a la función y le envío las cadenas
son_anagramas = SonAnagramas(cadena_uno, cadena_dos)

print(son_anagramas)
