'''
Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje
"Es paréntesis" sólo si el carácter leído es un paréntesis abierto o cerrado. En caso contrario
muestra el mensaje “No es paréntesis”.
'''

caracter = input("Ingrese un caracter: ")

if caracter == "(" or caracter == ")":
    print("Es un paréntesis")
else:
    print("No es un paréntesis")
