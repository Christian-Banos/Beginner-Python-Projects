class Televisor:
    
    def __init__(self, marca, canales):
        self.marca = marca
        self.canales = canales
        self.encendido = False
        self.canal = 0
        self.volumen = 0

    def __str__(self):
        return(
            f'Televisor {self.marca}\n'
            f'- Canales: {self.canales}\n'
            f'- Canal actual: {self.canal}\n'
            f'- Volumen actual: {self.volumen}\n'
        )

    def prender(self):
        if not self.encendido:
            self.encendido = True
            return(
                f'televisor encendiendose...📺\n'
                f'televisor encendido 🆗'
            )
        else:
            return f'El televisor ya se encuentra encendido 👌'
    
    def apagar(self):
        if self.encendido:
            self.encendido = False
            return(
                f'televisor apagandose...📺❌\n'
                f'televisor apagado 🆗'
            )
        else:
            return f'El televisor ya se encuentra apagado ❌'

    def ver_canal_siguiente(self):
        if self.encendido:
            self.canal += 1
            if self.canal > 100:
                self.canal = 0
            return f'Cambiando canal + 1.. Canal actual {self.canal}'
        else:
            return f'El televisor se encuentra apagado ❌. Enciendelo para cambiar de canales'

    def ver_canal_anterior(self):
        if self.encendido:
            self.canal -= 1
            if self.canal < 0:
                self.canal = 100
            return f'Cambiando canal - 1.. Canal actual {self.canal}'
        else:
            return f'El televisor se encuentra apagado ❌. Enciendelo para cambiar de canales'

    def cambiar_canal(self, numero):
        if self.encendido:
            self.canal = numero
            return f'Cambiando canal.. Canal actual {self.canal}'
        else:
            return f'El televisor se encuentra apagado ❌. Enciendelo para cambiar de canales'

    def subir_volumen(self):
        if self.encendido:
            if self.volumen < 20:
                self.volumen += 1
                return f'Subiendo volumen en 1..🔊. Volumen actual {self.volumen}'
            else:
                return f'Volumen al maximo 🔊. No se puede subir mas ❌'
        else:
            return f'El televisor se encuentra apagado ❌. Enciendelo para subir el volumen'
    
    def bajar_volumen(self):
        if self.encendido:
            if self.volumen > 0:
                self.volumen -= 1
                return f'Bajando volumen en 1..🔉. Volumen actual {self.volumen}'
            else:
                return f'Volumen al minimo 🔈. No se puede bajar mas ❌'
        else:
            return f'El televisor se encuentra apagado ❌. Enciendelo para bajar el volumen'


televisor = Televisor('Samsumg', 100)

while True:

    print(
        f'1. Encender televisor\n'
        f'2. Apagar televisor\n'
        f'3. Ver canal siguiente\n'
        f'4. Ver canal anterior\n'
        f'5. cabiar canal\n'
        f'6. Subir volumen\n'
        f'7. Bajar volumen\n'
        f'8. Ver propiedades del televisor\n'
        f'9. Salir\n'
    )

    option = input('Escoge una de las opciones: ')
    print()

    match option:
        case '1':
            print(televisor.prender())
        case '2':
            print(televisor.apagar())
        case '3':
            print(televisor.ver_canal_siguiente())
        case '4':
            print(televisor.ver_canal_anterior())
        case '5':
            canal = int(input('Introduce el numero del canal: '))
            print(televisor.cambiar_canal(canal))
        case '6':
            print(televisor.subir_volumen())
        case '7':
            print(televisor.bajar_volumen())
        case '8':
            print(televisor)
        case '9':
            print('Saliendo del programa')
            break
        case _:
            print('Opción incorrecta, Escoge una de las opciones: ')
    print()        