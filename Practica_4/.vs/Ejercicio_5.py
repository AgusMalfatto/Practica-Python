'''
Diseñar una función que determine si una lista de números enteros, cada número i entre 1
y n aparece i veces consecutivas.
Ejemplo: sonConsecutivos(5,[3,3,3,1,2,2,5,5,5,5,5,4,4,4,4]) --> verdadero
'''

def Telescopio(lista):
    control = 1
    posicion = 0
    # Recorro la lista
    for i in lista:
        contador = 0
        # Si el índice del número es igual al índice del nuevo número 
        if lista.index(i) == posicion:
            # Itero la cantidad de veces que debería estar el número
            while contador < i:
                # Si el número no es el que debería
                if lista[posicion] != i:
                    control = 0
                    break
                contador += 1
                posicion += 1
        if control == 0:
            break
    return control

cadena = [3, 3, 3, 1, 2, 2, 5, 5, 5, 5, 5, 4, 4, 4, 4]
conjunto = set(cadena) # Elimino los repetidos para obtener los números
cadena_Nueva = list(conjunto)
suma = 0

# Verifico que hayan la cantidad de elementos correctos
for i in cadena_Nueva:
    suma += i 
if suma == len(cadena):
    control = Telescopio(cadena)
else:
    control = 0

if control == 1:
    mensaje = "El telescopio es correcto."
else: 
    mensaje = "El telescopio es incorrecto"

print(mensaje)