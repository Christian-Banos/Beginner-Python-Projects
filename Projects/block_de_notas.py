class Note():
    def __init__(self, nombre, contenido):
        self.nombre = nombre
        self.contenido = contenido

    def __str__(self):
        return f'{self.nombre}: {"".join(contenido)}'

class block_notas():
    def __init__(self):
        self.notas = []

    def agregar_nota(self, titulo, contenido):
        nueva_nota = Note(titulo, contenido)
        self.notas.append(nueva_nota)

    def actualizar_nota(self, titulo, nuevo_titulo):
        for nota in self.notas:
            if nota.nombre == titulo:
                nota.nombre = nuevo_titulo
                print(f'Se ha actualizado el título de la nota de "{titulo}" a "{nuevo_titulo}"')
                return
        print('El título introducido no existe en la base de datos ❌')
        
    def obtener_notas(self):
        for idx, notas in enumerate(self.notas):
            print(f'{idx + 1}. {notas}')

    def eliminar_nota(self, indice):
        try:
            indice = int(indice) - 1
            if 0 <= indice < len(self.notas):
                nota_eliminada = self.notas.pop(indice)
                print(f'Nota eliminada: {nota_eliminada}')
            else:
                print("Índice inválido ❌")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    def elminar_notas(self):
        self.notas.clear()
        print('Todas las notas fueron eliminadas')

    def listar_notas(self):
        for nota in self.notas:
            print(nota)


nuevaNota = block_notas()

while True:

    print(
        '1. Agregar nota\n'
        '2. Acutalizar nota \n'
        '3. Obtener notas \n'
        '4. Eliminar nota \n'
        '5. Elminar todas las notas\n'
        '6. Listar todas las notas\n'
        '7. Salir')

    option = input('Introduce unas de las opciones: ')

    print()  

    match option:
        case '1':
            titulo = input('Introduce el nombre de la nota: ')
            contenido = input('Introduce el contenido de la nota: ')
            nuevaNota.agregar_nota(titulo, contenido)
        case '2':
            titulo = input('Introduce el titulo a cambiar: ')
            nuevo_titulo = input('Introduce el nuevo titulo: ')
            nuevaNota.actualizar_nota(titulo, nuevo_titulo)
        case '3':
            nuevaNota.obtener_notas()
            print()
        case '4':
            user_number = input('Introduce el numero de la nota a eliminar: ')
            nuevaNota.eliminar_nota(user_number)
        case '5':
            nuevaNota.elminar_notas()
        case '6':
            nuevaNota.listar_notas()
            print()
        case '7':
            print('Adios..')
            break
        case _:
            print('Opcion introducida incorrecta')   
