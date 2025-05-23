def mostrar_menu_login() -> str:
    print("Bienvenido al sistema de Biblioteca")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Vaciar datos")
    print("4. Cargar datos desde fichero externo")
    print("0. Salir")
    return input("Seleccione una opción: ")

def mostrar_menu_principal(alumno_filtrado: object = None) -> str:
    print("\n--- Menú principal ---")
    if alumno_filtrado:
        print(f"Alumno filtrado: {alumno_filtrado.nombre} ({alumno_filtrado.dni})")
    else:
        print("Alumno filtrado: Ninguno")
    print("1. Gestión de libros")
    print("2. Gestión de alumnos")
    print("3. Gestión de préstamos")
    print("4. Filtrar por alumno")
    print("5. Quitar filtro de alumno")
    print("0. Salir")
    return input("Seleccione una opción: ")

def mostrar_menu_libros() -> str:
    print("\n--- Gestión de libros ---")
    print("1. Agregar libro")
    print("2. Listar libros")
    print("3. Modificar libro")
    print("4. Eliminar libro")
    print("0. Volver")
    return input("Seleccione una opción: ")

def mostrar_menu_alumnos() -> str:
    print("\n--- Gestión de alumnos ---")
    print("1. Agregar alumno")
    print("2. Listar alumnos")
    print("3. Modificar alumno")
    print("4. Eliminar alumno")
    print("0. Volver")
    return input("Seleccione una opción: ")

def mostrar_menu_prestamos() -> str:
    print("\n--- Gestión de préstamos ---")
    print("1. Prestar libro")
    print("2. Devolver libro")
    print("3. Listar préstamos")
    print("0. Volver")
    return input("Seleccione una opción: ")
