'''# Crea una clase Contador que empiece en cero.
# Agrega métodos para aumentar, disminuir y resetear el contador.'''

class Contador:
    def __init__(self):
        self.contador = 0

    def aumentar(self):
        cantidad = int(input('Introduce la cantidad: '))
        if cantidad > 0:
            self.contador += cantidad
            print(f'La cantidad introducida {cantidad} es ha añadido correctamente. Contaddor actual {self.contador}')
        else:
            print('El valor introducido es incorrecto')

    def disminuir(self):
        cantidad = int(input('Introduce la cantidad: '))
        if cantidad > self.contador:
            print(f'No es posible disminuir esta cantidad, ya que es superior a {self.contador}')
        else:
            self.contador -= cantidad
            print(f'La cantidad {cantidad} se ha restado correctamente. Contador actual {self.contador}')

    def resetear_contador(self):
        if self.contador:
            self.contador = 0
            print(f'El contador se ha reseteado correctamente. Contador actual {self.contador}')
        else:
            print('Contador actual en 0')

contador = Contador()

while True:
    print()

    print('1. aumentar')
    print('2. disminuir')
    print('3. resetear contador')
    print('4. salir')

    options = input('Escoge una de las opciones: ')

    match options:
        case '1':
            try:
                contador.aumentar()
            except ValueError:
                print('Valor introducido invalido')
        case '2':
            try:
                contador.disminuir()
            except ValueError:
                print('Valor introducido invalido')
        case '3':
            contador.resetear_contador()
        case '4':
            print('Gracias por utilizar mi contador')
        case _:
            print('Valor introducido invalido')