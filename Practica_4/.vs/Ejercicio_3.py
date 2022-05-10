'''
Diseñar una función que determine si una lista de números enteros está ordenada de
menor a mayor y cada número i entre 1 y n aparece exactamente i veces.
Ejemplo:
para n = 5
esTelescopio(5,[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]) --> verdadero
'''

cantidad = int(input("Ingrese el valor del telescopio: "))
contador = 1
lista = []

while contador <= cantidad:
    for i in range(0, contador):
        lista.append(contador)
    
    contador += 1

print(lista)