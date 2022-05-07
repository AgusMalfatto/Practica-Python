'''
La ley de Chargaff dice que en el ADN de un organismo la cantidad de Adenina es la
misma que la de Tiamina, y la de Citosina es la misma que la de Guanina. Dada una
secuencia de nucleótidos del estilo de ATTACCAGTACA... podemos comprobar si cumple
dicha ley de la siguiente forma:
Contamos la cantidad de A, T, C y G presentes en la cadena y calculamos los coeficientes
donde NX indica la cantidad de nucleótidos del tipo X presentes en la secuencia.
Partiremos de una cadena que contiene una cantidad indeterminada de caracteres, que
solo pueden ser A, T, G ó C. Calcula a partir de dicha cadena los coeficientes a y c.
'''

cadena = input("Ingrese la cadena: ")
resultado = 0
a = 0
t = 0
c = 0
g = 0

# Recorro la cadena ingresada por el usuario
for i in cadena:
    # Compruebo qué letra es y sumo a su variable correspondiente
    if i == 'A':
        a += 1
    elif i == 'T':
        t += 1
    elif i == 'C':
        c += 1
    elif i == 'G':
        g += 1

# Resuelvo las cuentas solicitadas
resultado_A = (a - t) / (a + t) 
resultado_C = (c - g) / (c + g)

print(f"El coeficiente 'A' es: {resultado_A}")  
print(f"El coeficiente 'C' es: {resultado_C}")  