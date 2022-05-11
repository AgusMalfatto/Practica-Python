'''
Diseña una función que reciba una lista de cadenas y devuelva el prefijo común más
largo. Por ejemplo, la cadena "pol" es el prefijo común más largo de esta lista:
['poliedro', 'policia', 'polifona', 'polinizar', 'polaridad', 'politica']
'''

def Prefijo(cadena):
    control = 1
    for letra in range(0, len(cadena)):
        letra_nueva = cadena[0][letra]
        for palabra in cadena:
            if palabra[letra] != letra_nueva:
                control = 0
                break
        if control == 1:
            lista.append(letra_nueva)
        else:
            break
    
cadena = ['poliedro', 'policia', 'polifona', 'polinizar', 'polaridad', 'politica']
lista = []

Prefijo(cadena)
lista = ''.join(lista)
print(f"El prefijo más largo en las cadenas es: '{lista}'")