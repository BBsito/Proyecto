import shutil

DATOS_DIR = "datos"
ARCHIVOS = ["libros.csv", "alumnos.csv", "prestamos.csv"]

def vaciar_datos() -> None:
    for archivo in ARCHIVOS:
        ruta = f"{DATOS_DIR}/{archivo}"
        try:
            if archivo == "libros.csv":
                encabezado = "isbn,titulo,autor,curso,ejemplares,disponibles\n"
            elif archivo == "alumnos.csv":
                encabezado = "dni,nombre,curso\n"
            elif archivo == "prestamos.csv":
                encabezado = "alumno_dni,libro_isbn,fecha_prestamo,devuelto,fecha_devolucion\n"
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(encabezado)
            print(f"{archivo} vaciado correctamente.")
        except Exception as e:
            print(f"Error al vaciar {archivo}: {e}")

def cargar_datos_desde_fichero() -> None:
    print("¿Qué datos quieres cargar desde fuera?")
    print("1. Libros")
    print("2. Alumnos")
    print("3. Préstamos")
    print("0. Cancelar")
    opcion: str = input("Selecciona una opción: ").strip()
    if opcion == "1":
        nombre = "libros.csv"
    elif opcion == "2":
        nombre = "alumnos.csv"
    elif opcion == "3":
        nombre = "prestamos.csv"
    elif opcion == "0":
        print("Operación cancelada.")
        return
    else:
        print("Opción no válida.")
        return
    ruta_fuente: str = input(f"Introduce la ruta del fichero externo para {nombre}: ").strip()
    ruta_destino: str = f"{DATOS_DIR}/{nombre}"
    try:
        shutil.copy(ruta_fuente, ruta_destino)
        print(f"{nombre} cargado correctamente desde {ruta_fuente}.")
    except Exception as e:
        print(f"Error al cargar {nombre}: {e}")
