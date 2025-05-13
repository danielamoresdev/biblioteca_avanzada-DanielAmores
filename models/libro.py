class Libro:
    def __init__(self, titulo, autor, prestado=False):
        self.titulo = titulo
        self.autor = autor
        self.prestado = prestado

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Estado: {estado}"
    
    def alterar_estado(self, estado):
        self.prestado = estado