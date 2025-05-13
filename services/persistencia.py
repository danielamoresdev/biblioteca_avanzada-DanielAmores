import json

def cargar_usuarios(biblioteca):
    try:
        with open("data/usuarios.json", "r", encoding="utf-8") as fichero:
            datos = json.load(fichero)
            for u in datos:
                biblioteca.registrar_usuario(u["nombre"], u["rol"], u["libros_prestados"])
    except FileNotFoundError:
        pass

def guardar_usuarios(lista):
    lista_dict = []
    for l in lista:
        lista_dict.append({"nombre":l.nombre, "rol": l.rol, "libros_prestados": l.libros_prestados})
    with open("data/usuarios.json", "w", encoding="utf-8") as fichero:
        json.dump(lista_dict, fichero)
        
def cargar_libros(biblioteca):
    try:
        with open("data/libros.json", "r", encoding="utf-8") as fichero:
            datos = json.load(fichero)
            for u in datos:
                biblioteca.agregar_libro(u["titulo"], u["autor"], bool(u["prestado"]))
    except FileNotFoundError:
        pass

def guardar_libros(lista):
    lista_dict = []
    for l in lista:
        lista_dict.append({"titulo": l.titulo, "autor": l.autor, "prestado": int(l.prestado)})
    with open("data/libros.json", "w", encoding="utf-8") as fichero:
        json.dump(lista_dict, fichero)
        
def cargar_registro(historial):
    try:
        with open("data/historial.json", "r", encoding="utf-8") as fichero:
            datos = json.load(fichero)
            for r in datos:
                historial.registrar(r["accion"], r["usuario"], r["libro"], r["fecha"])
    except FileNotFoundError:
        pass
    
def guardar_registro(lista):
    with open("data/historial.json", "w", encoding="utf-8") as fichero:
        json.dump(lista, fichero)