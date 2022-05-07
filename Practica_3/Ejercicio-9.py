'''
ISBN-13 es un nuevo estandar para identificar libros. Usa 13 dígitos:
d1d2d3d4d5d6d7d8d9d10d11d12d13 .
El último dígito, es el dígito verificador y se calcula con la siguiente fórmula:
Si el dígito verificador es 10 se reemplaza por 0. El programa deberá permitir ingresar un
número como un string y mostrar el ISBN-13, ejemplo:
978013213080 ---> 9780132130806
'''

cadena = input("Ingrese la cadena: ")
resultado_parcial = 0
resultado = 0
control = 1 # Uso la variable control como interruptor

# Recorro la cadena
for numero in cadena:
    # Mi variable interruptor cambia de valor en cada iteración
    if control == 1:
        resultado_parcial += int(numero)
        control = 0
    else:
        resultado_parcial += (3 * int(numero))
        control = 1

# Realizo las operaciones
resultado_parcial = resultado_parcial % 10
resultado = 10 - resultado_parcial 

# Concateno el resultado a la cadena ingresada por el usuario
if resultado == 10:
    cadena += '0'
else:
    cadena += str(resultado)

print(cadena)