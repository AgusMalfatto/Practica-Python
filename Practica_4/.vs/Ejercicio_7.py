'''
La ciudad de Babilonia tiene una alta congestión de vehículos circulando por sus calles.
Las autoridades han decidido aplicar restricción vehicular para descongestionar la ciudad
en base a las patentes de los vehículos.
La patente de un vehículo es un string de cuatro letras y dos dígitos, y la restricción
depende sólo del penúltimo dígito. Por ejemplo, para la patente GEEA78, el dígito 7 es el
utilizado para evaluar la restricción.
La restricción vehícular de los días hábiles de la semana se encuentra ingresada en el
diccionario digitos, cuyas llaves son los días de la semanas, y cuyos valores son tuplas de
cuatro enteros que representan los dígitos con restricción de ese día.
• Implemente la función estaConRestriccion(digitos,dia, patente), que indique si el
    vehículo está o no con restricción.
• Implemente la función diasConRestriccion(digitos,patente), que retorne la lista de
    los días en que el vehículo no puede circular.
• Implemente la función diasSinRestriccion(digitos,patente), que retorne el conjunto
    de los días en que el vehículo sí puede circular.
digitos = {'lunes': (3, 4, 5, 6), 'martes': (7, 8, 9, 0),...,'miercoles': (1, 2, 3, 4), 'jueves':
 (5, 6, 7, 8), ... , 'viernes': (9, 0, 1, 2)}
estaConRestriccion(digitos, 'lunes', 'BBDT35') ---> True
diasConRestriccion(digitos, 'BBDT35') ---> ['lunes', 'miercoles']
diasSinRestriccion(digitos, 'BBDT35') ---> set(['jueves', 'martes', 'viernes'])

'''

def EstaConRestriccion(digitos, dias, patente):
    control = False
    dias = dias.lower()
    numero = patente[len(patente) - 2]
    if int(numero) in digitos[dias]:
        control = True
    
    return control

def DiasConRestriccion(digitos, patente):
    dias_con_restriccion = []
    numero = patente[len(patente) - 2]
    for i in digitos:
        if int(numero) in digitos[i]:
            dias_con_restriccion.append(i)
    return dias_con_restriccion

def DiasSinRestriccion(digitos, patente):
    dias_sin_restriccion = []
    numero = patente[len(patente) - 2]
    for i in digitos:
        if not(int(numero) in digitos[i]):
            dias_sin_restriccion.append(i)
    return dias_sin_restriccion


digitos = {
    'lunes': (3, 4, 5, 6), 
    'martes': (7, 8, 9, 0),
    'miercoles': (1, 2, 3, 4), 
    'jueves': (5, 6, 7, 8),
    'viernes': (9, 0, 1, 2)
    }

dia = 'viernes'
patente = "KJLD06"

dias_con_restriccion = DiasSinRestriccion(digitos, patente)

print(dias_con_restriccion)