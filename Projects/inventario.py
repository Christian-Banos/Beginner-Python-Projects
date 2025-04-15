'''# Crea una clase Producto con nombre, cantidad y precio.
# Crea una clase Inventario que maneje múltiples productos.
# Agrega métodos para:
# - Agregar productos
# - Vender productos
# - Mostrar todos los productos con su stock y valor total'''


class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f'nombre: {self.nombre} - cantidad: {self.cantidad} - precio: {self.precio}'

class Inventario:
    inventario_productos = {}

    def agregar_productos(self, producto):
        if producto.nombre in self.inventario_productos:
            self.inventario_productos[producto.nombre].cantidad += producto.cantidad
        else:
            self.inventario_productos[producto.nombre] = producto
            print(f'Se agregaron {producto.cantidad} unidades de "{producto.nombre}" al inventario.')

    def vender_productos(self, producto, cantidad):
        if nombre in self.inventario_productos:
            producto_stock = self.inventario_productos[nombre]
            #verificamos las unidades
            if producto_stock.cantidad < cantidad:
                print(f'No hay suficientes unidades de "{nombre}" en el inventario.')
            else:
                producto_stock.cantidad -= cantidad
                print(f'Se vendieron {cantidad} unidades de "{nombre}".')
        else:
            print('No se encontro ningún producto')

    def mostrar_productos(self):
        total_inventario = 0  # Valor total del inventario
        print('Productos en stock:')
        for nombre, info in self.inventario_productos.items():
            valor_total_producto = info.precio * info.cantidad  # Valor total de cada producto
            total_inventario += valor_total_producto  # Acumulamos el valor total del inventario
            print(f'Nombre: {nombre} / Cantidad: {info.cantidad} / Valor total del producto: {valor_total_producto}')
        print(f'Valor total del inventario: {total_inventario}')

inventario = Inventario()


while True:
    
    print('1. Crear producto')
    #print('2. Agregar productos')
    print('3. Vender productos')
    print('4. Mostrar stock')
    print('5. Salir')

    option = input('escoge una de las opciones: ')

    match option:
        case '1':
            nombre_producto = input('Introduce el nombre del producto: ')
            cantidad_producto = int(input('Introduce la cantidad: '))
            prcio_producto = int(input('Introduce el precio total: '))
            producto = Producto(nombre_producto, cantidad_producto, prcio_producto)
            inventario.agregar_productos(producto)
        case '2':
            '''nombre = input('Nombre del producto a agregar: ')
            if nombre in inventario.inventario_productos:
                cantidad = int(input('Cantidad a agregar: '))
                precio = inventario.inventario_productos[nombre].precio
                producto = Producto(nombre, cantidad, precio)
                inventario.agregar_productos(producto)
            else:
                print(f'El producto "{nombre}" no existe. Crea el producto primero con la opción 1.')'''
            pass

        case '3':
            nombre = input('Nombre del producto que quieres vender: ')
            cantidad = int(input('Cantidad a vender: '))
            inventario.vender_productos(nombre, cantidad)
        
        case '4':
            inventario.mostrar_productos()
        
        case '5':
            print('Salinedo del programa....')
            break
        case _:
            print('Valor introducido incorrecto')