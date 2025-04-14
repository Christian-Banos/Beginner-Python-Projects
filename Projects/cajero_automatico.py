'''
Crea una clase Cajero que simule un cajero automático. Debe tener los siguientes métodos:
	•	__init__(self, saldo_inicial)
	•	depositar(self, cantidad)
	•	retirar(self, cantidad)
	•	mostrar_saldo(self)

Extra: Agrega una protección para no permitir retirar más de lo que hay.
'''

class Cajero:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        print(f'Tu saldo inicial es de {self.saldo}')

    def depositar(self, cantidad):
        if cantidad <= 0:
            print('La cantidad debe ser mayor a 0')
        else:
            self.saldo += cantidad
            print(f'Se ha ingresado correctamente {cantidad} euros, saldo actual: {self.saldo}')
    
    def retirar(self, cantidad):
        if cantidad <= 0:
            print('La cantidad debe ser mayor a 0')
        elif cantidad > self.saldo:
            print(f'No se puede retirar una cantidad mayor a {self.saldo}')
        else:
            self.saldo -= cantidad
            print(f'Se ha retirado correctamente {cantidad} euros, saldo actual: {self.saldo}')

    def mostrar_saldo(self):
        print(f'El saldo actual de tu cuenta es de {self.saldo} euros')

cajero = Cajero(1000)

#opciones a escoger
while True:
    print()

    print('1. Despositar dinero')
    print('2. Retirar dinero')
    print('3. Verificar saldo disponible')
    print('4. Salir del cajero')

    option = input('Selecciona una acción: ')

    match option:
        case '1':
            try:
                cantidad = float(input('Cuanto deseas depositar: '))
                cajero.depositar(cantidad)
            except ValueError:
                print('Por favor ingresa un número válido')
                continue
        case '2':
            try:
                cantidad = float(input('Cuanto deseas retirar: '))
                cajero.retirar(cantidad)
            except ValueError:
                print('Por favor ingresa un número válido')
        case '3':
            cajero.mostrar_saldo()
        case '4':
            print('Gracias por utilizar mi cajero')
            break
        case _:
            print('Opción invalida, por favor selecciona una nueva')
