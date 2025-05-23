from models.alumno import Alumno

def agregar_alumno(alumnos: dict, dni: str, nombre: str, curso: str) -> bool:
    if dni in alumnos:
        print("Ya existe un alumno con ese DNI.")
        return False
    alumno: Alumno = Alumno(dni, nombre, curso)
    alumnos[dni] = alumno
    print("Alumno agregado correctamente.")
    return True

def listar_alumnos(alumnos: dict, alumno_filtrado) -> None:
    if alumno_filtrado:
        print(f"Alumno filtrado: {alumno_filtrado}")
        return
    if not alumnos:
        print("No hay alumnos registrados.")
        return
    for alumno in alumnos.values():
        print(alumno)

def modificar_alumno(alumnos: dict, dni: str) -> bool:
    alumno: Alumno = alumnos.get(dni)
    if not alumno:
        print("No se encontró el alumno con ese DNI.")
        return False
    print(f"Modificando alumno: {alumno}")
    nuevo_nombre: str = input(f"Nuevo nombre (actual: {alumno.nombre}) o Enter para dejar igual: ").strip()
    if nuevo_nombre:
        alumno.nombre = nuevo_nombre
    nuevo_curso: str = input(f"Nuevo curso (actual: {alumno.curso}) o Enter para dejar igual: ").strip()
    if nuevo_curso:
        alumno.curso = nuevo_curso
    print("Alumno modificado correctamente.")
    return True

def eliminar_alumno(alumnos: dict, dni: str) -> bool:
    if dni not in alumnos:
        print("No se encontró el alumno con ese DNI.")
        return False
    del alumnos[dni]
    print("Alumno eliminado correctamente.")
    return True
