class Alumno:
    def __init__(self, dni: str, nombre: str, curso: str) -> None:
        self.dni: str = dni
        self.nombre: str = nombre
        self.curso: str = curso
        self.prestamos: list = []

    def to_dict(self) -> dict:
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "curso": self.curso
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["dni"], d["nombre"], d["curso"])

    def __str__(self) -> str:
        return f"{self.nombre} ({self.dni}), Curso: {self.curso}"
