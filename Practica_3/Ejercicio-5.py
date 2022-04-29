'''
Escribir un programa que verifique si un string es una password correcta. Las reglas para
determinar si es correcta son:
    Debe tener como mínimo 8 caracteres.
    Sólo puede tener letras y dígitos.
    Como mínimo debe tener dos dígitos.
'''

import string


password = input("Ingrese su contraseña: ")

lista_password = list(password)

# Genero una cadena con todas las letras del abecedario (mayúsculas y minúsculas)
cadena = list(string.ascii_letters)
contador_letra = 0
contador_num = 0
control = 0

# Corroboro la longitud de la contraseña
if len(lista_password) > 8:
    # Recorro la contraseña ingresada caracter por caracter
    for i in lista_password:
        # Evaluo si el caracter pertenece al abecedario
        if i in cadena:
            contador_letra += 1
        # Evaluo que el caracter sea un número
        elif i.isdigit():
            contador_num += 1
        # Si no pertenece al abecedario ni es un número, la contraseña es incorrecta
        else:
            control = 1
            break
    
        
'''

                  PRIMERA FORMA QUE USÉ

if control == 0:
    for i in lista_password:
        if i.isdigit():
            lista_num.append(i)
            contador += 1
        else:
            lista_letra.append(i)
    if contador < 2:
        control = 1

if control == 0:
    for i in lista_letra:
        if i not in cadena :
            control = 1
    if len(lista_letra) == 0:
        control = 1
'''

if control != 1 and contador_num >= 2 and contador_letra > 0:
    mensaje = "La contraseña es correcta"
else:
    mensaje = "La contraseña no es correcta"

print(mensaje)