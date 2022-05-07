'''
Necesitamos buscar en diversas secuencias de ARN las posibles apariciones del codón
iniciador 'AUG', que marca el inicio de un gen. Como en una secuencia de ARN puede
haber más de un gen, deseamos conocer todas las posiciones en las que aparece dicho
codón. Para ello elaboraremos un programa que ingresará una cadena de caracteres que
representa una secuencia de ARN y comprobará que la secuencia de ARN contiene
únicamente los caracteres 'A','U', 'G' ó 'C'. En caso contrario, la secuencia es inválida y se
deberá imprimir un mensaje adecuado. 
'''

cadena = input("Ingrese la cadena: ")
lista = ['A', 'U', 'G', 'C']
control = 0

# Recorro la cadena
for letra in cadena:
    " Compruebo si la letra no está en la lista de letras válidas"
    if not(letra in lista):
        control = 1
        break

# Creo el mensaje correspondiente
if control == 0:
    mensaje = "La cadena es válida." 
else:
    mensaje = "La cadena es inválida." 

print(mensaje)