'''
Escribir funciones que, tomando como entrada una lista de números enteros, decida si la
lista:
está ordenada crecientemente.
está ordenada decrecientemente.
es gaspariforme. Se dice que un lista de n elementos es gaspariforme si todas sus
sumas parciales son no negativas, y la suma total es igual a 0. Las sumas parciales de
una lista a de n elementos está definida por
Si a = [ 10, 5, 2, 20, 6], n = 5
s0 = 10
s1 = 10 + 5 = 15
s2 = 10 + 5 + 2 = 15 + 2 = 17
s3 = 10 + 5 + 2 + 20 = 17 + 20 = 37
s4 = 10 + 5 + 2 + 20 + 6= 17 + 20 + 6 = 37 + 6 = 43
● es melchoriforme. Se dice que una lista es melchoriforme si alguno de sus elementos es
un centro . Un elemento es un centro si su valor coincide con la suma de los otros
elementos de la lista.
'''

# Función que determina si la lista es creciente
def Orden_Creciente(lista):
    creciente = True
    # Recorro la lista desde el segundo elemento hasta el fina
    for i in range(1, len(lista)):
        # Compruebo que si el elemento es menor al elemento anterior
        if lista[i] < lista[i - 1]:
            creciente = False # La lista no es creciente
            break
    return creciente    

# Función que determina si la lista es decreciente
def Orden_Decreciente(lista):
    decreciente = True
    # Recorro la lista desde el segundo elemento hasta el fina
    for i in range(1, len(lista)):
        # Compruebo que si el elemento es mmeyor al elemento anterior
        if lista[i] > lista[i - 1]:
            decreciente = False # La lista no es creciente
            break
    return decreciente   

# Función determina si la lista es gaspariforme
def Es_Gaspariforme(lista):
    gaspariforme = True
    suma = 0
    # Recorro la lista y sumo sus elementos
    for num in lista:
        suma += num
        # Compruebo si la suma parcial es menor a '0'
        if suma < 0:
            gaspariforme = False # La lista no es gaspariforme
            break
    # Compruebo si la suma total es distinto de '0'
    if suma != 0:
        gaspariforme = False # La lista no es gaspariforme
    return gaspariforme

# Función determina si la lista es melchoriforme
def Es_Melchoriforme(lista):
    centro = 0
    suma = 0
    melcho = False
    # Recorro la lista solo para sumar sus elementos
    for num in lista:
        suma += num
    # Recorro la lista 
    for num in lista:
        # Compruebo si el elemento es igual a la suma del resto de elementos de la lista
        if num == (suma - num):
            centro = num
            melcho = True
            break
    # Juntos dos elementos, si es melchoriforme o no, y cual es su centro
    melchoriforme = (melcho, centro)
    return melchoriforme

cont = 0
lista = []

# Ingreso de número 
while cont < 5:
    num = int(input("Ingrese un número: "))
    lista.append(num) 
    cont += 1

# Determino si es creciente o decreciente
if Orden_Creciente(lista):
    mensaje = "La lista es creciente"
else:
    if Orden_Decreciente(lista):
        mensaje = "La lista es decreciente"
    else:
        mensaje = "La lista no está ordenada"

# Determino si es gaspariforme o melchoriforme
if Es_Gaspariforme(lista):
    mensaje2 = "Es gaspariforme"
else:
    centro = Es_Melchoriforme(lista)
    if centro[0]:
        mensaje2 = "Es melchoriforme y su centro es " + str(centro[1])
    else:
        mensaje2 = "No es gaspariforme ni melchoriforme"

print(mensaje)
print(mensaje2)

