'''
Diseñar una función que determine si una lista de números enteros está ordenada de
menor a mayor y cada número i entre 1 y n aparece exactamente i veces.
Ejemplo:
para n = 5
esTelescopio(5,[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]) --> verdadero
'''

def Telescopio():
    posicion = 0
    control = 1
    # Recorro los números de la nueva lista
    for contador in cadena_Nueva:
        i = 0  
        # Itero en 'n' cantidad de veces se tiene que repetir el número
        while i < contador:
            # Si el número es distinto a su valor correspondiente
            if cadena[posicion] != contador:
                control = 0
                break
            posicion += 1
            i += 1
            
    return control


cadena = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
conjunto = set(cadena) # Elimino los repetidos para obtener los números
cadena_Nueva = list(conjunto)
suma = 0

# Verifico que hayan la cantidad de elementos correctos
for i in cadena_Nueva:
    suma += i 
if suma == len(cadena):
    control = Telescopio()
else:
    control = 0

if control == 1:
    mensaje = "El telescopio es correcto."
else: 
    mensaje = "El telescopio es incorrecto"

print(mensaje)
