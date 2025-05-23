from models.libro import Libro

def agregar_libro(libros: dict, isbn: str, titulo: str, autor: str, curso: str, ejemplares: int) -> bool:
    if isbn in libros:
        print("Ya existe un libro con ese ISBN.")
        return False
    libro: Libro = Libro(isbn, titulo, autor, curso, ejemplares)
    libros[isbn] = libro
    print("Libro agregado correctamente.")
    return True

def listar_libros(libros: dict, prestamos: list = None, alumno_filtrado: object = None) -> None:
    if alumno_filtrado and prestamos is not None:
        libros_prestados: list = [libros[p.libro_isbn] for p in prestamos if p.alumno_dni == alumno_filtrado.dni and not p.devuelto]
        if not libros_prestados:
            print("Este alumno no tiene libros prestados.")
            return
        print(f"Libros prestados a {alumno_filtrado.nombre}:")
        for libro in libros_prestados:
            print(libro)
        return

    if not libros:
        print("No hay libros registrados.")
        return
    for libro in libros.values():
        print(libro)

def modificar_libro(libros: dict, isbn: str) -> bool:
    libro: Libro = libros.get(isbn)
    if not libro:
        print("No se encontró el libro con ese ISBN.")
        return False
    print(f"Modificando libro: {libro}")
    nuevo_titulo: str = input(f"Nuevo título (actual: {libro.titulo}) o Enter para dejar igual: ").strip()
    if nuevo_titulo:
        libro.titulo = nuevo_titulo
    nuevo_autor: str = input(f"Nuevo autor (actual: {libro.autor}) o Enter para dejar igual: ").strip()
    if nuevo_autor:
        libro.autor = nuevo_autor
    nuevo_curso: str = input(f"Nuevo curso (actual: {libro.curso}) o Enter para dejar igual: ").strip()
    if nuevo_curso:
        libro.curso = nuevo_curso
    while True:
        nuevo_ejemplares: str = input(f"Nuevos ejemplares (actual: {libro.ejemplares}) o Enter para dejar igual: ").strip()
        if not nuevo_ejemplares:
            break
        if nuevo_ejemplares.isdigit() and int(nuevo_ejemplares) > 0:
            diferencia: int = int(nuevo_ejemplares) - libro.ejemplares
            libro.ejemplares = int(nuevo_ejemplares)
            libro.disponibles += diferencia
            break
        else:
            print("Por favor, ingrese un número válido o deje en blanco.")
    print("Libro modificado correctamente.")
    return True

def eliminar_libro(libros: dict, isbn: str) -> bool:
    if isbn not in libros:
        print("No se encontró el libro con ese ISBN.")
        return False
    del libros[isbn]
    print("Libro eliminado correctamente.")
    return True
