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

def Busca_ADN(lista, separador):
    adn = lista.split(separador, 1) 
    lista_ADN.append(adn[0]) 

if "ATG" in cadena:
    lista_cadena = cadena.split("ATG")
    for i in lista_cadena:
        for fin in final:
            if fin in i:
                Busca_ADN(i, fin)


for adn in lista_ADN:
    if (len(adn) % 3) != 0:
        indice = lista_ADN.index(adn)
        lista_ADN.pop(indice)

print(lista_ADN)