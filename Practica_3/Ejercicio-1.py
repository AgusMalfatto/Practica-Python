'''
Escribir una función que reciba una cadena que contiene un número entero largo y
devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe
'1234567890', debe devolver '1.234.567.890'
'''

num = input("Ingrese un número: ")

lista = list(num)

# Recorro el número iniciando 3 unidades antes del final (primer punto de mil), recorro cada tres unidades hasta el dígito de mayor peso
for i in range(len(lista)-4, -1, -3):
    # Coloco un punto en delante del dígito 
    lista.insert(i + 1, ".")

numero = "".join(lista)

print(numero)


'''
SEGUNDA FORMA -- USANDO .FORMAT

print(f"{num:,.0f}".format(num).replace(',', '.'))

'''