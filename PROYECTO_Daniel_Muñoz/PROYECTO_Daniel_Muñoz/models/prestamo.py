from datetime import date

class Prestamo:
    def __init__(self, alumno_dni: str, libro_isbn: str, fecha_prestamo: str = None, devuelto: bool = False, fecha_devolucion: str = None) -> None:
        self.alumno_dni: str = alumno_dni
        self.libro_isbn: str = libro_isbn
        self.fecha_prestamo: str = fecha_prestamo if fecha_prestamo is not None else date.today().isoformat()
        self.devuelto: bool = devuelto
        self.fecha_devolucion: str = fecha_devolucion

    def devolver(self) -> None:
        self.devuelto = True
        self.fecha_devolucion = date.today().isoformat()

    def to_dict(self) -> dict:
        return {
            "alumno_dni": self.alumno_dni,
            "libro_isbn": self.libro_isbn,
            "fecha_prestamo": self.fecha_prestamo,
            "devuelto": self.devuelto,
            "fecha_devolucion": self.fecha_devolucion
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["alumno_dni"], d["libro_isbn"], d.get("fecha_prestamo"), d.get("devuelto", False), d.get("fecha_devolucion"))

    def __str__(self) -> str:
        estado: str = "Devuelto" if self.devuelto else "En préstamo"
        return f"Libro ISBN {self.libro_isbn} a alumno DNI {self.alumno_dni} ({estado})"
