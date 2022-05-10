resultado = [[],[],[],[]]
mayor = []
lista = [
    ['A', 'T', 'C', 'C', 'A', 'G', 'C', 'T'],
    ['G', 'G', 'G', 'C', 'A', 'A', 'C', 'T'],
    ['A', 'T', 'G', 'G', 'A', 'T', 'C', 'T'],
    ['A', 'A', 'G', 'C', 'A', 'A', 'C', 'C'],
    ['T', 'T', 'G', 'G', 'A', 'A', 'C', 'T'],
    ['A', 'T', 'G', 'C', 'C', 'A', 'T', 'T'],
    ['A', 'T', 'G', 'G', 'C', 'A', 'C', 'T']
]

# Recorro el rango de listas dentro de la lista
for gen in range(0, 8):
    a = 0
    c = 0
    g = 0
    t = 0
    # Recorro la lista
    for i in lista:
        if i[gen] == 'A':
            a += 1
        elif i[gen] == 'C':
            c += 1
        elif i[gen] == 'G':
            g += 1
        elif i[gen] == 'T':
            t += 1
    # Agrego los resultados a la lista resultado
    resultado[0].append(a)
    resultado[1].append(c)
    resultado[2].append(g)
    resultado[3].append(t)
    # Busco el mayor
    if (a >= c) and (a >= g) and (a >= t):
        mayor.append('A')
    elif (c >= a) and (c >= g) and (c >= t):
        mayor.append('C')
    elif (g >= c) and (g >= c) and (g >= t):
        mayor.append('G')
    else:
        mayor.append('T')

for i in resultado:
    print(i)

print(mayor)