from tiendalibros.modelo.libro import Libro         
from tiendalibros.modelo.carro_compra import CarroCompras
from tiendalibros.modelo.excepciones import LibroExistenteError
from tiendalibros.modelo.excepciones import ExistenciasInsuficientesError
from tiendalibros.modelo.carro_compra import CarroCompras
from tiendalibros.modelo.item_compra import ItemCompra

class LibroError(Exception):
    pass

class LibroExistenteError(LibroError):
    def __init__(self, titulo: str, isbn: str):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return f"El libro con titulo {self.titulo} y isbn: {self.isbn} ya existe en el catálogo"

class LibroAgotadoError(LibroError):
    def __init__(self, titulo: str, isbn: str):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return f"El libro con titulo {self.titulo} y isbn {self.isbn} esta agotado"

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, titulo: str, isbn: str, cantidad_a_comprar: int, existencias: int):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias = existencias

    def __str__(self):
        return f"El libro con titulo {self.titulo} y isbn {self.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias}"

class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int) -> Libro:
        if isbn in self.catalogo:
            raise LibroExistenteError(titulo, isbn)
        libro = Libro(titulo, isbn, precio, existencias)
        self.catalogo[isbn] = libro
        return libro

    def agregar_libro_a_carrito_de_compras(self, libro, cantidad):
        try:
            self.carrito.agregar_item(libro, cantidad)

        except (LibroAgotadoError, ExistenciasInsuficientesError) as e:
            print(e)


    def retirar_item_de_carrito(self, isbn: str):
        self.carrito.quitar_item(isbn)