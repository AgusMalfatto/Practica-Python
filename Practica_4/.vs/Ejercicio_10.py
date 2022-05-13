'''
En el juego ScrabbleTM, cada letra tiene asociado un valor numérico. El puntaje total de una
palabra es la suma de los valores numéricos de cada letra. Las letras más comunes tienen
menor valor que las letras menos comunes. Los puntos asociados a cada letra se muestran
en la siguiente tabla:
puntos letras
1 A,E,I,L,N,O,R,S,T, U
2 D,G
3 B,C,M,P
4 F,H,V,W,Y
5 K
8 J,X
10 Q,Z
Escribir un programa que calcule y muestre el puntaje de una palabre. Crear un
diccionario para almacenar la tabla anterior.
'''

'''
def puntaje_palabra(palabra):
    puntaje = 0
    for l in palabra:
        for puntos, letras in diccionario.items(): La funciòn .items() divide el diccionario en key y value
            if l in letras:
                puntaje += puntos
    return puntaje

'''

def Calcular_Puntos(diccionario, palabra):
    puntaje = 0
    palabra = palabra.upper()
    # Recorro cada letra de la palabra
    for letra in palabra:
        # Recorro el diccionario de puntos
        for i in diccionario:
            if letra in diccionario[i]:
                puntaje += i
                break
    return puntaje
        

diccionario = {
    1: ['A','E','I','L','N','O','R','S','T','U'],
    2: ['D','G'],
    3: ['B','C','M','P'],
    4: ['F','H','V','W','Y'],
    5: ['K'],
    8: ['J','X'],
    10: ['Q','Z']
}

palabra = input("Ingrese la palabra: ")

puntaje = Calcular_Puntos(diccionario, palabra)

print(f"El puntaje es: {puntaje}")