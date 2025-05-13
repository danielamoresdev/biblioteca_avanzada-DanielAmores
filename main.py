import os
from services.biblioteca import *
from utils.menu import *
from time import sleep
clear = lambda: os.system('clear')
bib = Biblioteca()

while True:
    mostrar_menu()
    opcion = input("Introduce la opción que desea > ")
    
    match opcion:
        case '1':
            clear()
            print("---- Agregar libro ----")
            titulo = input("Introduzca el título > ")
            autor = input("Introduzca el autor > ")
            print(bib.agregar_libro(titulo, autor))
            input("Enter para continuar")
            clear()
        case '2':
            clear()
            print("---- Eliminar libros ----")
            titulo = input("Introduzca el título > ")
            print(bib.eliminar_libro(titulo))
            input("Enter para continuar")
            clear()
        case '3':
            clear()
            print("---- Registrar usuario ----")
            nombre = input("Introduzca el nombre > ")
            rol = input("Introduzca el rol (lector / administrador) > ")
            print(bib.registrar_usuario(nombre, rol))
            input("Enter para continuar")
            clear()
        case '4':
            clear()
            print("---- Eliminar usuario ----")
            nombre = input("Introduzca el nombre > ")
            print(bib.eliminar_usuario(nombre))
            input("Enter para continuar")
            clear()
        case '5':
            clear()
            print("---- Prestar libro ----")
            titulo = input("Introduzca el titulo > ")
            nombre = input("Introduzca el nombre del usuario >")
            print(bib.prestar_libro(titulo, nombre))
            input("Enter para continuar")
            clear()
        case '6':
            clear()
            print("---- Devolver libro ----")
            titulo = input("Introduzca el titulo > ")
            nombre = input("Introduzca el nombre del usuario >")
            print(bib.devolver_libro(titulo, nombre))
            input("Enter para continuar")
            clear()
        case '7':
            clear()
            bib.mostrar_libros_disponibles()
            input("Enter para continuar")
            clear()
        case '8':
            clear()
            bib.mostrar_libros_prestados()
            input("Enter para continuar")
            clear()
        case '9':
            clear()
            bib.mostrar_usuarios()
            input("Enter para continuar")
            clear()
        case '10':
            clear()
            print("Volcando datos...")
            bib.volcar_datos()
            print("Datos volcados")
            input("Enter para continuar")
            clear()
        case '11':
            clear()
            print("Exportando datos...")
            bib.exportar_csv()
            print("Datos exportados")
            input("Enter para continuar")
            clear()
        case '0':
            print("Volcando datos...")
            bib.volcar_datos()
            print("Datos volcados")
            print("Saliendo del sistema...")
            break
        case _:
            print("La opción introducida no es válida.")
