'''
Escribir un programa que permita ingresar las coordenadas (x,y) de un punto en el plano y
verifique si el punto está dentro del círculo con centro en (0,0) y radio 10, o está fuera o en
la circunferencia. Mostrar los mensajes adecuados.
'''

from math import sqrt

x = float(input("Ingrese la coordenada 'X': "))
y = float(input("Ingrese la coordenada 'Y': "))

hipotenusa = sqrt((x**2)+(y**2))

if hipotenusa < 10:
    mensaje = "El punto está dentro de la circunferencia"
elif hipotenusa == 10:
    mensaje = "El punto está en el límite de la circunferencia"
else:
    mensaje = "El punto está fuera de la circunferencia"

print(mensaje)