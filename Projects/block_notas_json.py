#To do
import json

class Note():
    def __init__(self, descripcion, estado=False):
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f'{self.descripcion} - {"Completada" if self.estado else "Pendiente"}'

    def to_dict(self):
        return {'descripcion': self.descripcion, 'estado': self.estado}

class Block_notas():
    def __init__(self):
        self.notas = []

    def agregar_tareas(self, descripcion, estado=False):
        nueva_nota = Note(descripcion, estado)
        self.notas.append(nueva_nota)
        print(f'{nueva_nota} : Se agrego correctamente al block de notas')
        self.guardar_en_archivo('notas.json')
        print()

    def mostrar_notas(self):
        if not self.notas:
            print('No hay tareas agregadas')
        else:
            for i, nota in enumerate(self.notas, 1):
                print(f'{i}. {nota}')

    def marcar_completada(self, descripcion):
        for nota in self.notas:
            if nota.descripcion == descripcion:
                nota.estado = True
                print(f'{descripcion} a cambiado a {nota.estado}')
                self.guardar_en_archivo('notas.json')
                return
        print(f'{descripcion} no se encuentra registrada en el block de notas')

    def eliminar_nota(self, descripcion):
        for nota in self.notas:
            if nota.descripcion == descripcion:
                self.notas.remove(nota)
                print(f'{descripcion} se ha borrado del block de notas')
                self.guardar_en_archivo('notas.json')
                return

        print(f'{descripcion} no se encuentra registrada en el block de notas')

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as f:
            json.dump([nota.to_dict() for nota in self.notas], f)
        print('✅ Notas guardadas en el archivo.')
    
    def carga_de_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as f:
                datos = json.load(f)
                self.notas = [Note(d['descripcion'], d['estado']) for d in datos]
                print('✅ Notas cargadas del archivo.')
        except FileNotFoundError:
            print('📂 No se encontró un archivo previo. Se comenzará con una lista vacía.')

nueva_nota = Block_notas()
nueva_nota.carga_de_archivo('notas.json')

while True:
    print('1. Agregar nota')
    print('2. Mostrar notas')
    print('3. Marcar nota como completada')
    print('4. Eliminar nota')
    print('5. Salir')

    option = input('Escoge una de las siguientes opciones: ')

    print()

    match option:
        case '1':
            nueva_tarea = input('Agrega una nueva tarea: ').lower()
            nueva_nota.agregar_tareas(nueva_tarea)
        case '2':
            nueva_nota.mostrar_notas()
        case '3':
            tarea = input('Introduce la tarea que haz finalizado: ').lower()
            nueva_nota.marcar_completada(tarea)
        case '4':
            nota_a_eliminar = input('Introduce la nota que quieres eliminar: ').lower()
            nueva_nota.eliminar_nota(nota_a_eliminar)
        case '5':
            print('Saliste del block de notas')
            nueva_nota.guardar_en_archivo('notas.json')
            break
        case _:
            print('Opcion elegida incorrecta')
