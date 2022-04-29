cadena = input("Ingrese la cadena: ")

# Creo una lista, en la que cada elemento es una lista de las letras dispuestas en el teléfono
lista = (("A", "B", "C"), ("D", "E", "F"), ("G", "H", "I"), ("J", "K", "L"), ("M", "N", "O"), 
("P", "Q", "R", "S"), ("T", "U", "V"), ("W", "X", "Y", "Z"))

lista_cadena = list(cadena)

numero = []

# Recorro la cadena ingresada por el usuario
for i in lista_cadena:
    # Recorro la lista creada anteriormente
    for k in lista:
        if i in k:
            indice = lista.index(k)
            # Las letras comienzan en el número 2 en el teclado telefónico, por eso sumo 2 al índice
            numero.append(indice + 2)
            break

'''
for i in lista_cadena:
    control = 0
    for k in lista:
        for m in k:
            if i == m:
                indice = lista.index(k)
                numero.append(indice + 2)
                control = 1
                break
        if control == 1:
            break
'''
print(f"El número es: ", end="")
for i in numero:
    numero_final = int(i)
    print(numero_final, end="")