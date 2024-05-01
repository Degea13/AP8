import sys


from tiendalibros.modelo.tienda_libros import TiendaLibros
from tiendalibros.modelo.tienda_libros import TiendaLibros
from tiendalibros.modelo.excepciones import LibroAgotadoError, ExistenciasInsuficientesError, LibroExistenteError


class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.mostrar_carrito_de_compras,
            "5": self.salir
            }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda La Mayoria!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print("4. Mostrar carrito de compras")
        print("5. Salir")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def adicionar_un_libro_a_catalogo(self):
        try:
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el título del libro: ")
            precio = float(input("Ingrese el precio del libro: "))
            existencias = int(input("Ingrese la cantidad de existencias del libro: "))
            libro = self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print(f"El libro '{libro.titulo}' ha sido añadido al catálogo.")
        except LibroExistenteError as e:
            print(e)
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el precio.")

    def agregar_libro_a_carrito_de_compras(self):
        try:
            isbn = input("Ingrese el ISBN del libro que desea agregar al carrito: ")
            cantidad = int(input("Ingrese la cantidad de unidades del libro que desea agregar: "))
            libro = self.tienda_libros.catalogo.get(isbn)
            print(f"El libro '{libro.titulo}' ha sido añadido al carrito de compras.")
            if libro is None:
                print("El libro con el ISBN proporcionado no está en el catálogo.")
                return
            self.tienda_libros.agregar_libro_a_carrito_de_compras(libro, cantidad)
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para la cantidad.")

    def retirar_libro_de_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro que desea retirar del carrito: ")
        self.tienda_libros.retirar_item_de_carrito(isbn)
        print("El libro ha sido retirado del carrito de compras.")

    def mostrar_carrito_de_compras(self):
        print("Carro de compras:")
        for item in self.tienda_libros.carrito.items:
            subtotal = item.libro.precio * item.cantidad
            print(f"- {item.cantidad}x {item.libro.titulo} (Subtotal: ${subtotal:.2f})")
        print(f"Total de la compra: ${self.tienda_libros.carrito.calcular_total():.2f}")

    def menu_principal(self):
        while True:
            print("\n======= MENU PRINCIPAL =======")
            print("1. Adicionar un libro al catálogo")
            print("2. Agregar un libro al carrito de compras")
            print("3. Retirar un libro del carrito de compras")
            print("4. Mostrar Carrito de compras ")
            print("5. Salir")

            opcion = input("Ingrese el número de la opción que desea ejecutar: ")

            if opcion == "1":
                self.adicionar_un_libro_a_catalogo()
            elif opcion == "2":
                self.agregar_libro_a_carrito_de_compras()
            elif opcion == "3":
                self.retirar_libro_de_carrito_de_compras()
            elif opcion == "4":
                self.mostrar_carrito_de_compras()
            elif opcion == "5":
                print("Gracias por utilizar nuestra tienda de libros. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    ui = UIConsola()
    ui.menu_principal()