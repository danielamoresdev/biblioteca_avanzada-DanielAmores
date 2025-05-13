from models.libro import *
from models.historial import *
from models.usuario import *
from services.persistencia import *
from services.csv import *

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.historial = Historial()
            
    def agregar_libro(self, titulo, autor, prestado=False):
        if not self._obtener_libro(titulo):
            libro = Libro(titulo, autor, prestado)
            self.libros.append(libro)
            return "Libro agregado"
        return "El libro ya está registrado"
    
    def eliminar_libro(self, titulo):
        libro = self._obtener_libro(titulo) 
        if self._obtener_libro(titulo):
            self.libros.remove(libro)
            return "Libro eliminado"
        return "El libro no está registrado"

    def registrar_usuario(self, nombre, rol, libros_prestados=[]):
        if not self._obtener_usuario(nombre):
            if rol.lower() == 'administrador' or rol.lower() == 'lector':
                usuario = Usuario(nombre, rol, libros_prestados)
                self.usuarios.append(usuario)
                return "Usuario registrado"
            return "Rol no válido"
        return "El usuario ya está registrado"
        
    def eliminar_usuario(self, nombre):
        usuario = self._obtener_usuario(nombre) 
        if usuario:
            for l in usuario.libros_prestados:
                self._obtener_libro(l).alterar_estado(False)
            self.usuarios.remove(usuario)
            return "Usuario eliminado"
        return "El usuario no está registrado"
        
    def prestar_libro(self, titulo, nombre):
        usuario = self._obtener_usuario(nombre)
        libro = self._obtener_libro(titulo)
        
        if usuario is None:
            return "El usuario no existe"
        if libro is None:
            return "El libro no existe"
        if libro.prestado:
            return "El libro ya está prestado"
        
        usuario.prestar_libro(libro)
        libro.prestado = True
        self.historial.registrar("Prestar", usuario.nombre, libro.titulo)
        return f"{titulo} prestado a {nombre}"
        
    def devolver_libro(self, titulo, nombre):
        usuario = self._obtener_usuario(nombre)
        libro = self._obtener_libro(titulo)
        
        if usuario is None:
            return "El usuario no existe"
        if libro is None:
            return "El libro no existe"
        if not libro.prestado:
            return "El libro no está en ningún préstamo"
        
        if usuario.devolver_libro(libro):
            libro.alterar_estado(False)
            self.historial.registrar("Devolver", usuario.nombre, libro.titulo)
            return "Libro devuelto"
            
    def mostrar_libros_disponibles(self):
        print("====== LIBROS DISPONIBLES ======")
        for l in self.libros:
            if not l.prestado:
                print(f"Titulo: {l.titulo} | Autor: {l.autor}")
                
    def mostrar_libros_prestados(self):
        print("====== LIBROS PRESTADOS ======")
        for l in self.libros:
            if l.prestado:
                print(f"Titulo: {l.titulo} | Autor: {l.autor}")
    
    def mostrar_usuarios(self):
        for u in self.usuarios:
            print(u)
    
    def cargar_datos(self):
        cargar_usuarios(self)
        cargar_libros(self)
        cargar_registro(self.historial)
    
    def volcar_datos(self):
        guardar_usuarios(self.usuarios)
        guardar_libros(self.libros)
        guardar_registro(self.historial.registros)
    
    def exportar_csv(self):
        exportar_usuarios(self.usuarios)
        exportar_libros(self.libros)
        exportrar_registros(self.historial.registros)
    
    def _obtener_usuario(self, nombre):
        for u in self.usuarios:
            if u.nombre.lower() == nombre.lower():
                return u
        return None
    
    def _obtener_libro(self, titulo):
        for l in self.libros:
            if l.titulo.lower() == titulo.lower():
                return l
        return None