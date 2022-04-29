num1 = input('Ingrese un número binario: ')
num2 = input('Ingrese otro número binario: ')
acarreo = 0
resultado = ''

# Igualar el largo de los números binarios
if len(num1) > len(num2):
    num2 = num2.zfill(len(num1))
elif len(num1) < len(num2):
    num1 = num1.zfill(len(num2))

# Sumar los números
for d in range(len(num1)-1,-1,-1):
    # Sumamos el número acarreado
    r = acarreo
    # Sumamos si el dígito es 1
    if num1[d] == '1':
        r += 1
    if num2[d] == '1':
        r += 1
    # Sumamos r al resultado
    if r % 2 == 1:
        resultado = '1' + resultado
    else:
        resultado = '0' + resultado
    # Actualizamos el número acarreado 
    if r == 2 or r == 3:
        acarreo = 1
    else:
        acarreo = 0

# Sumar lo que queda en el acarreo si es necesario
if acarreo == 1:
    resultado = '1' + resultado

print(resultado)