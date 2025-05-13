class Usuario:
    def __init__(self, nombre, rol, libros_prestados=[]):
        self.nombre = nombre
        self.rol = rol.capitalize()
        self.libros_prestados = libros_prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro.titulo)

    def devolver_libro(self, titulo):
        for libro in self.libros_prestados:
            print(libro)
            print(titulo)
            if libro.lower() == titulo.titulo.lower():
                self.libros_prestados.remove(libro)
                return libro
        return None

    def __str__(self):
        return f"{self.nombre} | Rol: {self.rol} | Libros prestados: {[libro.titulo for libro in self.libros_prestados]}"