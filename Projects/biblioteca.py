'''
🔹 Ejercicio 2: Biblioteca

Crea una clase Libro con atributos como titulo, autor, y disponible. 
Luego, crea una clase Biblioteca que contenga una lista de libros y tenga métodos para:
	•	Agregar libros
	•	Buscar libros por título
	•	Prestar un libro
	•	Devolver un libro'''

class Libro:
    def __init__(self, titulo, autor, disponible):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

class Biblioteca:
    def __init__(self):
        self.lista_libros = []
        self.libros_prestados = []

    def agregar_libros(self, nuevo_libro):
        if nuevo_libro in self.lista_libros:
            print('El libro ya esta registrado..')
        else:
            self.lista_libros.append(nuevo_libro)
            print(f'el {nuevo_libro.titulo} se ha registrado correctmente')
            
    def buscar_libro_por_titulo(self, titulo):
        encontrado = False
        for libro in self.lista_libros:
            if libro.titulo == titulo:
                print(f'Este es el libro que buscas: "{libro.titulo} del autor {libro.autor}. Disponibilidad: {libro.disponible}"')
                encontrado = True
                break
            
        if not encontrado:
            print('No se ha encontrado ningun libro con ese titulo')
           

    def prestar_libros(self, titulo):
        for libro in self.lista_libros:
            if libro.titulo == titulo:
                self.lista_libros.remove(libro)
                self.libros_prestados.append(libro)
                print('El libro fue prestado correctamente...')
                return
        print('No se ha encontrado ningún libro con este título')

    def devolver_libros(self, titulo):

        for libro in self.libros_prestados:
            if libro.titulo == titulo:
                self.libros_prestados.remove(libro)
                self.lista_libros.append(libro)
                print(f'El libro {libro.titulo} se devolvio correctamente.')
                return
            
        print(f'{titulo} este libro no nos pertenece')

    def ver_inventario(self):
        print('Inventario actual:')
        for libro in self.lista_libros:
            print(f'{libro.titulo} del autor {libro.autor}. Disponible: {libro.disponible}')      

biblioteca = Biblioteca()

while True:
    print()

    print('1. Agregar libros')
    print('2. Buscar libro por titulo: ')
    print('3. Prestar libros: ')
    print('4. Devolver libros: ')
    print('5. Ver inventario actual')
    print('&. Salir')

    options = input('Selecciona una accion: ')

    match options:
        case '1':
            titulo = input('Introduce el titulo del libro: ')
            autor = input('Introduce el autor: ')
            disnibilidad = True
            libro = Libro(titulo, autor, disnibilidad)
            biblioteca.agregar_libros(libro)
            print(f'El libro {titulo} del autor {autor} se agrego correctamente a la Biblioteca')
        case '2':
            libro = input('Introduce el libro que quieres buscar: ')
            biblioteca.buscar_libro_por_titulo(libro)
        case '3':
            titulo = input('Introduce el nombre del libro que quieres alquilar: ')
            biblioteca.prestar_libros(titulo)
        case '4':
            titulo = input('Introduce el nombre del libro que quieres devolver: ')
            biblioteca.devolver_libros(titulo)
        case '5':
            biblioteca.ver_inventario()
        case '6':
            print('Gracias por utilizar nuestra biblioteca. Hasta pronto')
            break
        case _:
            print('Opcion incorrecta, intentalo denuevod')