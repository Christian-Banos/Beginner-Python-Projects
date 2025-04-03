'''
calculate body BMI
'''

def bmi(peso, altura):
    imc = peso / ((altura / 100) ** 2) 
    print(f'Tu BMI es de {imc:.2f}')
    
    if imc > 40:
        print('Estás con obesidad grado 3 (mórbida o extrema) 😔')
    else:
        if imc > 35:
            print('Estás con obesidad grado 2')
        elif imc > 30:
            print('Estas con obesidad grado 1')
        elif imc > 25:
            print('Estas con sobrepeso')
        elif imc > 18:
            print('Estas con el peso ideal')
        else:
            print('Estas con peso bajo')
    
    return imc

try:
    peso = float(input('Introduce tu peso en kilogramos: '))
    altura = float(input('Introduce tu altura en centimetros: '))
    resultado = bmi(peso, altura)
except ValueError:
    print('Error: Por favor introduce números válidos')
    

