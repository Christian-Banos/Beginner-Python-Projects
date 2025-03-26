"""
Programa para verificar si un año es bisiesto.
Un año es bisiesto si:
1. Es divisible por 4 Y
2. No es divisible por 100 O es divisible por 400
"""

def es_bisiesto(year):
    return year > 0 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))

try:
    anio = int(input('Por favor ingrese un año: '))

    if anio < 0:
        print('El año no puede ser inferior a 0')
    else:
        if es_bisiesto(anio):
            print(f'{anio} es un año bisiesto')
        else:
            print(f'{anio} no es un año bisiesto')
except ValueError:
    print('Por favor ingreso un numero entero válido')
