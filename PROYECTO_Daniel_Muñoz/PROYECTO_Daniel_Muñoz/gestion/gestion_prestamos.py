from models.prestamo import Prestamo

def prestar_libro(libros: dict, alumnos: dict, prestamos: list, dni: str, isbn: str) -> bool:
    alumno = alumnos.get(dni)
    libro = libros.get(isbn)
    if not alumno:
        print("Alumno no encontrado.")
        return False
    if not libro:
        print("Libro no encontrado.")
        return False
    if libro.disponibles <= 0:
        print("No hay ejemplares disponibles de este libro.")
        return False
    for prestamo in prestamos:
        if prestamo.alumno_dni == dni and prestamo.libro_isbn == isbn and not prestamo.devuelto:
            print("El alumno ya tiene este libro prestado y no lo ha devuelto.")
            return False
    if libro.prestar():
        prestamo: Prestamo = Prestamo(alumno_dni=dni, libro_isbn=isbn)
        alumno.prestamos.append(prestamo)
        prestamos.append(prestamo)
        print(f"Libro '{libro.titulo}' prestado a {alumno.nombre}.")
        return True
    else:
        print("No se pudo realizar el préstamo.")
        return False

def devolver_libro(libros: dict, alumnos: dict, prestamos: list, dni: str, isbn: str) -> bool:
    alumno = alumnos.get(dni)
    libro = libros.get(isbn)
    if not alumno:
        print("Alumno no encontrado.")
        return False
    if not libro:
        print("Libro no encontrado.")
        return False
    for prestamo in prestamos:
        if prestamo.alumno_dni == dni and prestamo.libro_isbn == isbn and not prestamo.devuelto:
            prestamo.devolver()
            libro.devolver()
            print(f"Libro '{libro.titulo}' devuelto por {alumno.nombre}.")
            return True
    print("Préstamo no encontrado o ya devuelto.")
    return False

def listar_prestamos(prestamos: list, alumno_filtrado) -> None:
    if alumno_filtrado:
        encontrados: list = [p for p in prestamos if p.alumno_dni == alumno_filtrado.dni]
        if not encontrados:
            print(f"No hay préstamos registrados para el alumno con DNI {alumno_filtrado.dni}.")
            return
        for prestamo in encontrados:
            print(prestamo)
        return
    if not prestamos:
        print("No hay préstamos registrados.")
        return
    for prestamo in prestamos:
        print(prestamo)
