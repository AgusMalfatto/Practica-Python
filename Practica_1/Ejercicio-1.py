'''
Diseña un programa que lea la edad de dos personas y diga quién es más joven, la
primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso,
hazlo saber con un mensaje adecuado
'''

edad_uno = input("Ingrese la primer edad: ")
edad_dos = input("Ingrese la segunda edad: ")

if edad_uno < edad_dos:
    print("La primer persona es más jóven.")
elif edad_dos < edad_uno:
    print("La segunda persona es más jóven.")
else:
    print("Tienen la misma edad.")