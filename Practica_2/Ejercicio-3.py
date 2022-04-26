'''
Escribir un programa que muestre, de a diez números por línea y separados por un
blanco, todos los números entre 100 y 1000 que sean divisibles por 5 y 6
'''
cont = 0
for num in range(100, 1001):
    calculo_5 = num / 5 - num // 5
    calculo_6 = num / 6 - num // 6
    if calculo_5 == 0 and calculo_6 == 0:
        if cont < 9:
            print(num, end=" ")
            cont += 1
        else:
            print(num)
            cont = 0