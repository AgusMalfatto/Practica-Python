'''
Diseñar una función que determine si una lista de números enteros, cada número i entre 1
y n aparece i veces consecutivas.
Ejemplo: sonConsecutivos(5,[3,3,3,1,2,2,5,5,5,5,5,4,4,4,4]) --> verdadero
'''

def Telescopio(lista):
    control = 1
    contador = 0
    while contador < lista[contador]:
        posicion = contador
        if lista[contador] != lista[posicion]:
            control = 0
            break
        contador += 1
    return control

cadena = [3, 3, 3, 1, 2, 2, 5, 5, 5, 5, 5, 4, 4, 4, 4]
control = Telescopio(cadena)

if control == 1:
    mensaje = "El telescopio es correcto."
else: 
    mensaje = "El telescopio es incorrecto"

print(mensaje)