import csv

def exportar_usuarios(usuarios):
    with open('data/usuarios.csv', 'w', newline="\n") as csvfile:
        campos = ["nombre", "rol", "libros_prestados"]
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
    
        for u in usuarios:
            writer.writerow({
                "nombre": u.nombre, "rol": u.rol, "libros_prestados": u.libros_prestados
            })

def exportar_libros(libros):
    with open('data/libros.csv', 'w', newline="\n") as csvfile:
        campos = ["titulo", "autor", "prestado"]
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
    
        for l in libros:
            writer.writerow({
                "titulo": l.titulo, "autor": l.autor, "prestado": l.prestado
            })

def exportrar_registros(registros):
    with open('data/registros.csv', 'w', newline="\n") as csvfile:
        campos = ["accion", "usuario", "libro", "fecha"]
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
    
        for r in registros:
            writer.writerow({
                "accion": r["accion"], "usuario": r["usuario"], "libro": r["libro"], "fecha": r["fecha"]
            })