from login import login, registrar_usuario
from menu import mostrar_menu_login
from gestion.gestion_datos import vaciar_datos, cargar_datos_desde_fichero
from menu import mostrar_menu_principal, mostrar_menu_libros, mostrar_menu_alumnos, mostrar_menu_prestamos
from utilidades.pedir_informacion import pedir_datos_libro, pedir_datos_alumno, pedir_dni_alumno, pedir_isbn_libro, mostrar_mensaje
from utilidades import almacenamiento
from gestion.gestion_libros import agregar_libro, listar_libros, modificar_libro, eliminar_libro
from gestion.gestion_alumnos import agregar_alumno, listar_alumnos, modificar_alumno, eliminar_alumno
from gestion.gestion_prestamos import prestar_libro, devolver_libro, listar_prestamos

def main():
    while True:
        opcion: str = mostrar_menu_login()
        if opcion == "1":
            if login():
                break
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            confirm: str = input("¿Seguro que quieres vaciar todos los datos? (s/n): ").strip().lower()
            if confirm == "s":
                vaciar_datos()
            else:
                print("Operación cancelada.")
        elif opcion == "4":
            cargar_datos_desde_fichero()
        elif opcion == "0":
            print("¡Hasta luego!")
            return
        else:
            print("Opción no válida.")

    libros = {}
    alumnos = {}
    prestamos: list = []
    almacenamiento.cargar_datos_objetos(libros, alumnos, prestamos)
    alumno_filtrado = None

    while True:
        opcion = mostrar_menu_principal(alumno_filtrado)
        if opcion == "1":
            while True:
                subop: str = mostrar_menu_libros()
                if subop == "1":
                    datos = pedir_datos_libro()
                    agregar_libro(libros, *datos)
                elif subop == "2":
                    listar_libros(libros, prestamos, alumno_filtrado)
                elif subop == "3":
                    if alumno_filtrado:
                        modificar_libro(libros, next((p.libro_isbn for p in prestamos if p.alumno_dni == alumno_filtrado.dni and not p.devuelto), None))
                    else:
                        isbn: str = pedir_isbn_libro()
                        modificar_libro(libros, isbn)
                elif subop == "4":
                    if alumno_filtrado:
                        mostrar_mensaje("No se puede eliminar libros desde el filtro de alumno.")
                    else:
                        isbn: str = pedir_isbn_libro()
                        eliminar_libro(libros, isbn)
                elif subop == "0":
                    break
                else:
                    mostrar_mensaje("Opción no válida.")

        elif opcion == "2":
            while True:
                subop: str = mostrar_menu_alumnos()
                if subop == "1":
                    datos = pedir_datos_alumno()
                    agregar_alumno(alumnos, *datos)
                elif subop == "2":
                    listar_alumnos(alumnos, alumno_filtrado)
                elif subop == "3":
                    if alumno_filtrado:
                        modificar_alumno(alumnos, alumno_filtrado.dni)
                    else:
                        dni: str = pedir_dni_alumno()
                        modificar_alumno(alumnos, dni)
                elif subop == "4":
                    if alumno_filtrado:
                        eliminar_alumno(alumnos, alumno_filtrado.dni)
                        alumno_filtrado = None
                    else:
                        dni: str = pedir_dni_alumno()
                        eliminar_alumno(alumnos, dni)
                elif subop == "0":
                    break
                else:
                    mostrar_mensaje("Opción no válida.")

        elif opcion == "3":
            while True:
                subop: str = mostrar_menu_prestamos()
                if subop == "1":
                    if alumno_filtrado:
                        isbn: str = pedir_isbn_libro()
                        prestar_libro(libros, alumnos, prestamos, alumno_filtrado.dni, isbn)
                    else:
                        dni: str = pedir_dni_alumno()
                        isbn: str = pedir_isbn_libro()
                        prestar_libro(libros, alumnos, prestamos, dni, isbn)
                elif subop == "2":
                    if alumno_filtrado:
                        isbn: str = pedir_isbn_libro()
                        devolver_libro(libros, alumnos, prestamos, alumno_filtrado.dni, isbn)
                    else:
                        dni: str = pedir_dni_alumno()
                        isbn: str = pedir_isbn_libro()
                        devolver_libro(libros, alumnos, prestamos, dni, isbn)
                elif subop == "3":
                    listar_prestamos(prestamos, alumno_filtrado)
                elif subop == "0":
                    break
                else:
                    mostrar_mensaje("Opción no válida.")

        elif opcion == "4":
            dni: str = pedir_dni_alumno()
            alumno = alumnos.get(dni)
            if alumno:
                alumno_filtrado = alumno
                print(f"Alumno {alumno.nombre} ({alumno.dni}) seleccionado para filtrado.")
            else:
                print("Alumno no encontrado.")

        elif opcion == "5":
            alumno_filtrado = None
            print("Filtro de alumno eliminado.")

        elif opcion == "0":
            almacenamiento.guardar_datos_objetos(libros, alumnos, prestamos)
            print("¡Hasta luego!")
            break

        else:
            mostrar_mensaje("Opción no válida.")

if __name__ == "__main__":
    main()
