'''
Los biólogos usan una secuencia de letras A, C, T, y G para modelar un genoma. Un gen es
un subcadena de un genoma que comienza después de la tripleta ATG y termina con una
tripleta TAG, TAA, ó TGA. La longiutd de una cadena de gen es un múltiplo de 3 y el gen
no contiene a las tripletas ATG, TAG, TAA y TGA. Escribir un programa que permita
ingresar un genoma y muestre todos los genes en el genoma. Si en la cadena no se
encuentran genes, el programa mostrará un mensaje acorde. Ejemplo:
si la cadena es TTATGTTTTAAGGATGGGGCGTTAGTT, el programa mostrará:
TTT
GGGCGT
Si la cadena es TGTGTGTATAT entonces se deberá mostrar "no se encontraron genes".
'''

cadena = input("Ingrese la cadena: ")
lista_cadena = []
lista_ADN = []
adn = ""
inicio = "ATG"
final = ["TAG", "TAA", "TGA"]

# Función que corta el ADN y lo guarda en una lista
def Busca_ADN(lista, separador):
    adn = lista.split(separador, 1) # Separo el genoma en dos partes usando la tripleta que indica el final del gen (primero el gen, segundo desecho)
    lista_ADN.append(adn[0]) # Agrego el gen a la lista

# Compruebo que exista la tripleta 'ATG' en el genoma
if "ATG" in cadena:
    #Separo el genoma usando la tripleta 'ATG' como separador
    lista_cadena = cadena.split("ATG")
    # Recorro la lista generada antes
    for i in lista_cadena:
        # Recorro la lista con las tripletas que marcan el final de un gen
        for fin in final:
            # Compruebo qué tripleta me marca el fin del gen
            if fin in i:
                # Envío la porción del genoma junto con la tripleta final
                Busca_ADN(i, fin)


# Recorro la lista de ADNs encontrados
for adn in lista_ADN:
    # Si el largo del ADN no es múltiplo de 3 lo elimino de la lista
    if (len(adn) % 3) != 0:
        indice = lista_ADN.index(adn)
        lista_ADN.pop(indice)

print(lista_ADN)