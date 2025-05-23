import re

def pedir_isbn_libro() -> str:
    patron_isbn = re.compile(r"^\d{10}$|^\d{13}$")
    while True:
        isbn: str = input("ISBN (10 o 13 dígitos, solo números, sin guiones ni espacios): ").strip()
        if not patron_isbn.match(isbn):
            print("El ISBN debe tener exactamente 10 o 13 dígitos numéricos, sin guiones ni letras.")
        else:
            return isbn

def pedir_datos_libro():
    isbn: str = pedir_isbn_libro()

    titulo: str = input("Título: ").strip()
    while not titulo or len(titulo) < 3:
        print("El título no puede estar vacío y debe tener al menos 3 caracteres.")
        titulo = input("Título: ").strip()

    autor: str = input("Autor: ").strip()
    while not autor or len(autor) < 3:
        print("El autor no puede estar vacío y debe tener al menos 3 caracteres.")
        autor = input("Autor: ").strip()

    patron_curso = re.compile(r'^\d{1}[A-Z]{3}$')
    while True:
        curso: str = input("Curso (ej: 1ESO): ").strip()
        if not patron_curso.match(curso):
            print("Formato de curso incorrecto. Debe ser 1 número y 3 letras mayúsculas (ej: 1ESO, 2DAW).")
        else:
            break

    while True:
        ejemplares_str: str = input("Número de ejemplares: ").strip()
        if not ejemplares_str.isdigit() or int(ejemplares_str) <= 0:
            print("Introduce un número entero positivo para los ejemplares.")
        else:
            ejemplares: int = int(ejemplares_str)
            break

    return isbn, titulo, autor, curso, ejemplares

def pedir_dni_alumno() -> str:
    patron_dni = re.compile(r'^\d{8}[A-Z]$')
    while True:
        dni: str = input("DNI del alumno (8 números y 1 letra mayúscula, ej: 12345678A): ").strip()
        if not patron_dni.match(dni):
            print("Formato de DNI incorrecto. Debe tener 8 números y una letra mayúscula (ej: 12345678A).")
        else:
            return dni

def pedir_datos_alumno():
    dni: str = pedir_dni_alumno()

    nombre: str = input("Nombre: ").strip()
    while not nombre or len(nombre) < 3:
        print("El nombre no puede estar vacío y debe tener al menos 3 caracteres.")
        nombre = input("Nombre: ").strip()

    patron_curso = re.compile(r'^\d{1}[A-Z]{3}$')
    while True:
        curso: str = input("Curso (ej: 1ESO): ").strip()
        if not patron_curso.match(curso):
            print("Formato de curso incorrecto. Debe ser 1 número y 3 letras mayúsculas (ej: 1ESO, 2DAW).")
        else:
            break

    return dni, nombre, curso

def mostrar_mensaje(mensaje: str) -> None:
    print(mensaje)
