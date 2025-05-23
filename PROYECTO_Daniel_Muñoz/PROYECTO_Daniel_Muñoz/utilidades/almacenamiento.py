import csv
from models.libro import Libro
from models.alumno import Alumno
from models.prestamo import Prestamo

def guardar_datos_objetos(libros: dict, alumnos: dict, prestamos: list, ruta: str = "datos") -> None:
    with open(f"{ruta}/libros.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["isbn", "titulo", "autor", "curso", "ejemplares", "disponibles"])
        for libro in libros.values():
            writer.writerow([libro.isbn, libro.titulo, libro.autor, libro.curso, libro.ejemplares, libro.disponibles])
    with open(f"{ruta}/alumnos.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["dni", "nombre", "curso"])
        for alumno in alumnos.values():
            writer.writerow([alumno.dni, alumno.nombre, alumno.curso])
    with open(f"{ruta}/prestamos.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["alumno_dni", "libro_isbn", "fecha_prestamo", "devuelto", "fecha_devolucion"])
        for prestamo in prestamos:
            writer.writerow([
                prestamo.alumno_dni,
                prestamo.libro_isbn,
                prestamo.fecha_prestamo,
                str(prestamo.devuelto),
                prestamo.fecha_devolucion if prestamo.fecha_devolucion else ""
            ])

def cargar_datos_objetos(libros: dict, alumnos: dict, prestamos: list, ruta: str = "datos") -> None:
    libros.clear()
    try:
        with open(f"{ruta}/libros.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                libro = Libro(
                    row["isbn"],
                    row["titulo"],
                    row["autor"],
                    row["curso"],
                    int(row["ejemplares"]),
                    int(row["disponibles"])
                )
                libros[libro.isbn] = libro
    except FileNotFoundError:
        pass

    alumnos.clear()
    try:
        with open(f"{ruta}/alumnos.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                alumno = Alumno(
                    row["dni"],
                    row["nombre"],
                    row["curso"]
                )
                alumnos[alumno.dni] = alumno
    except FileNotFoundError:
        pass

    prestamos.clear()
    try:
        with open(f"{ruta}/prestamos.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                prestamo = Prestamo(
                    row["alumno_dni"],
                    row["libro_isbn"],
                    row["fecha_prestamo"],
                    row["devuelto"] == "True",
                    row["fecha_devolucion"] if row["fecha_devolucion"] else None
                )
                prestamos.append(prestamo)
    except FileNotFoundError:
        pass
