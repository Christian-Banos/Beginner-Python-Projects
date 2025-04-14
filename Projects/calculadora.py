class Calculadora:
    def __init__(self):
        pass
    def sumar(self, entero1, entero2):
        resultado_suma =  entero1 + entero2
        print(f'la suma de los dos numeros es: {resultado_suma}')

    def resta(self, entero1, entero2):
        resultado_resta =  entero1 - entero2
        print(f'la resta de los dos numeros es: {resultado_resta}')

    def multiplicacion(self, entero1, entero2):
        resultado_multiplicacion =  entero1 * entero2
        print(f'la multiplicacion de los dos numeros es: {resultado_multiplicacion}')

    def division(self, entero1, entero2):
        try:
            resultado_division =  entero1 / entero2
            print(f'la division de los dos numeros es: {resultado_division}')
        except ZeroDivisionError:
            print('No se puede dividir un numero por 0')


calculadora = Calculadora()

while True:
    print()

    
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    print('5. salir')

    option = input('Elige alguna de las operaciones: ')

    match option:
        case '1':
            try:
                entero1 = int(input('Introduce el primer numero entero: '))
                entero2 = int(input('Introduce el segundo numero entero: '))
                calculadora.sumar(entero1, entero2)
            except ValueError:
                print('Valor introducido invalido')
        case '2':
            try:
                entero1 = int(input('Introduce el primer numero entero: '))
                entero2 = int(input('Introduce el segundo numero entero: '))
                calculadora.resta(entero1, entero2)
            except ValueError:
                print('Valor introducido invalido')
        case '3':
            try:
                entero1 = int(input('Introduce el primer numero entero: '))
                entero2 = int(input('Introduce el segundo numero entero: '))
                calculadora.multiplicacion(entero1, entero2)
            except ValueError:
                print('Valor introducido invalido')
        case '4':
            try:
                entero1 = int(input('Introduce el primer numero entero: '))
                entero2 = int(input('Introduce el segundo numero entero: '))
                calculadora.division(entero1, entero2)
            except ValueError:
                print('Valor introducido invalido')
        case '5':
            print('Gracias por utilizar mi calculadora')
            break
        case _:
            print('Opción invalida, por favor selecciona una nueva')