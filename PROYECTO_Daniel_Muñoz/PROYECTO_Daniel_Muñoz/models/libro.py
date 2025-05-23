class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str, curso: str, ejemplares: int, disponibles: int = None) -> None:
        self.isbn: str = isbn
        self.titulo: str = titulo
        self.autor: str = autor
        self.curso: str = curso
        self.ejemplares: int = ejemplares
        self.disponibles: int = disponibles if disponibles is not None else ejemplares

    def prestar(self) -> bool:
        if self.disponibles > 0:
            self.disponibles -= 1
            return True
        return False

    def devolver(self) -> bool:
        if self.disponibles < self.ejemplares:
            self.disponibles += 1
            return True
        return False

    def to_dict(self) -> dict:
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "curso": self.curso,
            "ejemplares": self.ejemplares,
            "disponibles": self.disponibles
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            d["isbn"], d["titulo"], d["autor"], d["curso"], d["ejemplares"], d.get("disponibles", d["ejemplares"])
        )

    def __str__(self) -> str:
        return f"{self.titulo} (ISBN: {self.isbn}) - Disponibles: {self.disponibles}/{self.ejemplares}"
