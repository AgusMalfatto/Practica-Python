'''
Diseñar una función que genere una lista en forma de telescopio .
Ejemplo: genTelescopio(5) --> [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
'''

def Telescopio(cantidad):
    contador = 1
    while contador <= cantidad:
        for i in range(0, contador):
            lista.append(contador)
        
        contador += 1

cantidad = int(input("Ingrese el valor del telescopio: "))
contador = 1
lista = []

Telescopio(cantidad)

print(lista)