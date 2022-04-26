'''
Escribir una función que reciba una cadena que contiene un número entero largo y
devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe
'1234567890', debe devolver '1.234.567.890'
'''

num = int(input("Ingrese un número: "))

print(f"{num:,.0f}".format(num).replace(',', '.'))