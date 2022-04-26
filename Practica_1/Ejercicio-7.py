'''
Escribir un programa que permita ingresar el mes y el año y muestre la cantidad de días
del mes. Por ejemplo, si el usuario ingresa mes 2 y año 2000, el programa debe responder
que Febrero 2000 tiene 29 días. Si el usuario ingresa mes 3 y año 2005, el programa
responderá que Marzo 2005 tiene 31 días.
'''


lista_mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
trinta_uno = [1, 3, 5, 7, 8, 10, 12]
treinta_dias = [4, 6, 9, 11]

def Calculo_Bisiesto(anio):
    calculo = anio / 4 - anio // 4
    if calculo == 0:
        dias_febrero = 29
    else:
        dias_febrero = 28
    return dias_febrero


def Calculo_Mes(mes):
    for i in lista_mes:
        if lista_mes[mes-1] == i:
            el_mes = lista_mes[mes-1]
            break
    if mes in treinta_dias:
        dias = 30
    elif mes in trinta_uno:
        dias = 31
    else:
        dias = Calculo_Bisiesto(anio)
    mes_anio = (el_mes, dias)
    return mes_anio


mes = int(input("Ingrese el mes: "))
while mes <= 0 or mes > 12:
    mes = int(input("Mes erroneo, ingrese un mes válido (entre 1 y 12): "))

anio = int(input("Ingrese el año: "))

mes_anio = Calculo_Mes(mes)
mes_real, dias = mes_anio

print(f"{mes_real} del {anio} tiene {dias} días")

