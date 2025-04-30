'''
- **Propiedades**
    - `encendido` (booleano), inicializa en `false`
    - `velocidad` (número), inicializa en 0
    - `marca` (string)
    - `modelo` (número)
    - `patente` (string)
- **Constructor**
    - pide como argumentos `marca`, `modelo`, `patente` y los asigna a sus respectivas propiedades
- **Métodos**
    - **`arrancar()`** pone `encendido` en `true`
    - **`apagar()`** pone `encendido` en `false`
    - **`acelerar()`** suma 10 a `velocidad` y actualiza dicha propiedad
    - **`desacelerar()`** resta 10 a `velocidad` y actualiza dicha propiedad
    - **`toString()`** devuelve un *string* con la siguiente plantilla `${marca} ${modelo}, patente ${patente}`
'''

class Auto:
    def __init__(self, marca, modelo, patente):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.encendido = False
        self.velocidad = 0

    def __str__(self):
        return f'Marca: {self.marca}. Modelo: {self.modelo}. Patente: {self.patente}'

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            print('Encendiendo coche...')
            print('Coche encendido 🚗')
        else:
            print('El coche esta encendido 🚗')

    def apagar(self):
        if self.encendido:
            if self.velocidad == 0:
                self.encendido = False
                print('Apagando coche...')
                print('Coche Apagado 🚘')
            else:
                print('Coche en marcha 🚗🚗. NO SE PUEDE APAGAR')
        else:
            print('El coche ya esta apagado 🚘')

    def acelerar(self):
        if self.encendido:
            self.velocidad += 10
            print('Acelerando coche...🚗🚗🚗')
            print('Velocidad actual: ', self.velocidad)
        else:
            print('El coche no puede acelerar ya que esta pagado!!')

    def desacelerar(self):
        if self.encendido:
            self.velocidad -= 10
            print('Desacelerando coche...🚗')
            print('Velocidad actual: ', self.velocidad)
        else:
            print('El coche no puede acelerar ya que esta pagado!!')

coche = Auto('audi', 'A4', 12345)

while True:

    print('1. Encender coche')
    print('2. Apagar coche')
    print('3. Acelerar coche')
    print('4. Desacelerar coche')
    print('5. Propiedades del coche')
    print('6. Salir')

    opcion = input('Escoge una de las siguientes opciones: ')

    match (opcion):
        case '1':
            coche.arrancar()
        case '2':
            coche.apagar()
        case '3':
            coche.acelerar()
        case '4':
            coche.desacelerar()
        case '5':
            print(coche)
        case '6':
            print('Saliendo...')
            break
        case _:
            print('Opción incorrecta, itentalo denuevo')