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
cadena = list(string.ascii_letters)
contador_letra = 0
contador_num= 0
control = 0

if len(lista_password) < 8:
    control = 1

if control == 0:
    for i in lista_password:
        if i in cadena:
            contador_letra += 1
        elif i.isdigit():
            contador_num += 1
        else:
            control = 1
            break
        
'''
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

if control == 1 or contador_num < 2 or contador_letra == 0:
    mensaje = "La contraseña no es correcta"
else:
    mensaje = "La contraseña es correcta"

print(mensaje)