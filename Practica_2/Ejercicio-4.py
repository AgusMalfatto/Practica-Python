'''
Construir un programa que permita multiplicar dos números enteros positivos empleando
el método denominado multiplicación rusa. Este método permite calcular el producto de N
por M dela siguiente forma:
'''

num1 = int(input("Ingrese un primer número: "))
while num1 <= 0:
    num1 = int(input("Error, ingrese un número positivo: "))
num2 = int(input("Ingrese un segundo número: "))
while num2 <= 0:
    num2 = int(input("Error, ingrese un número positivo: "))

resta = num1//2
multiplicacion = num2 * 2
lista_num1 = [num1, resta]
lista_num2 = [num2, multiplicacion]

while resta > 1:
    resta //= 2
    multiplicacion *= 2
    lista_num1.append(resta)
    lista_num2.append(multiplicacion)

suma = 0

for i in lista_num1:
    calculo = i % 2
    if calculo != 0:
        index = lista_num1.index(i)
        suma += lista_num2[index]

print(f"La resta del primer número: {lista_num1}")
print(f"La multiplicación del segundo número: {lista_num2}")
print(f"La multiplicación es: {suma}")


