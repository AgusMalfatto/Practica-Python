'''
Haz un programa que lea dos cadenas que representen sendos números binarios. A
continuación, el programa mostrará el número binario que resulta de sumar ambos (y que
será otra cadena). Si, por ejemplo, el usuario introduce las cadenas '100' y '111', el
programa mostrará como resultado la cadena '1011'.
Nota: El procedimiento de suma con acarreo que implementes deberá trabajar
directamente con la representación binaria leída.
'''

num1 = input("Ingrese el primer número binario: ")
num2 = input("Ingrese el segundo número binario: ")

acarreo = 0
resultado_final = ''

'''num1_bin = int(num_1)
num2_bin = int(num_2)

lista1 = list(num_1)
lista2 = list(num_2)
'''

# Agrego los '0' necesarios para igualar el largo de ambos números
if len(num1) < len(num2):
    num1 = num1.zfill(len(num2))
elif len(num2) < len(num1):
    num2 = num2.zfill(len(num1))

# Recorro el número desde el último dígito hasta el primero.
for i in range(len(num1)-1, -1, -1):
    resultado = acarreo # 'resultado' almacena la suma de los bits de cada posición, incluyendo el acarreo.

    # Sumo los bits de cada posición.
    if num1[i] == '1':
        resultado += 1
    if num2[i] == '1':
        resultado += 1
    
    # Si el resultado es impar se agrega un 1 al resultado final.
    if resultado % 2 == 1:
        resultado_final = '1' + resultado_final
    else:
        resultado_final = '0' + resultado_final
    
    # Verifico si hay que acarrear un '1'.
    if resultado >= 2:
        acarreo = 1
    else: 
        acarreo = 0

if acarreo == 1:
    resultado_final = '1' + resultado_final

print(resultado_final)

'''

                  PRIMERA FORMA QUE USÉ

if len(lista1) < len(lista2):
    largo = len(lista2)
else:
    largo = len(lista1)

nueva_lista1 = []
nueva_lista2 = []
nueva_lista = []
acarreo = 0

for number in lista1:
    nueva_lista1.insert(0, number)

for number in lista2:
    nueva_lista2.insert(0, number)

largo_lista1 = len(lista1)
largo_lista2 = len(lista2)

for i in range(largo):
    if (i < largo_lista1) and (i < largo_lista2):
        num1 = nueva_lista1[i]
        num2 = nueva_lista2[i]
        suma = int(num1) + int(num2)
        if suma <= 1:
            if acarreo == 0:
                nueva_lista.insert(0, suma)
            else:
                if suma == 1:
                    nueva_lista.insert(0, 0)
                else:
                    nueva_lista.insert(0, 1)
                    acarreo = 0
        else:
            if acarreo == 1:
                nueva_lista.insert(0, 1)
                
            else:
                nueva_lista.insert(0, 0)
                acarreo = 1
    elif i < len(lista1):
        if acarreo == 1 and nueva_lista1[i] == '1':
            nueva_lista.insert(0, 0)
        elif acarreo == 1 and nueva_lista1[i] == '0':
            nueva_lista.insert(0, 1)
            acarreo = 0
        elif acarreo == 0 and nueva_lista1[i] == '1':
            nueva_lista.insert(0, 1)
        elif acarreo == 0 and nueva_lista1[i] == '0':
            nueva_lista.insert(0, 0)
    elif i < len(lista2):
        if acarreo == 1 and nueva_lista2[i] == '1':
            nueva_lista.insert(0, 0)
        elif acarreo == 1 and nueva_lista2[i] == '0':
            nueva_lista.insert(0, 1)
            acarreo = 0
        elif acarreo == 0 and nueva_lista2[i] == '1':
            nueva_lista.insert(0, 1)
        elif acarreo == 0 and nueva_lista2[i] == '0':
            nueva_lista.insert(0, 0)

if acarreo == 1:
    nueva_lista.insert(0, 1)

        
print(nueva_lista)
'''
