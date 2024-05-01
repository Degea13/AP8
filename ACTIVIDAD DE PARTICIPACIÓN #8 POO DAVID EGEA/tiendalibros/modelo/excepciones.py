class LibroExistenteError(Exception):
    pass

class LibroAgotadoError(Exception):
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return f"El libro con titulo {self.titulo} y isbn {self.isbn} esta agotado"

class ExistenciasInsuficientesError(Exception):
    def __init__(self, titulo, isbn, cantidad_disponible):
        self.titulo = titulo
        self.isbn = isbn
        self.cantidad_disponible = cantidad_disponible

    def __str__(self):
        return f"Existencias insuficientes para el libro '{self.titulo}' (ISBN: {self.isbn}). " \
               f"Cantidad disponible: {self.cantidad_disponible}"
