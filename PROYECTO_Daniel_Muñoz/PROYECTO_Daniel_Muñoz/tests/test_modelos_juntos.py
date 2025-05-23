import unittest
from models.libro import Libro
from models.alumno import Alumno
from models.prestamo import Prestamo

class TestModelosJuntos(unittest.TestCase):
    def setUp(self):
        self.libros = {}
        self.alumnos = {}
        self.prestamos = []

        self.libro = Libro("111", "2006", "Dani", "1DAW", 2)
        self.alumno = Alumno("22222222B", "Lorena Muñoz", "2ESO")
        self.libros[self.libro.isbn] = self.libro
        self.alumnos[self.alumno.dni] = self.alumno

    def test_prestar_y_devolver(self):
        self.assertTrue(self.libro.prestar())
        prestamo = Prestamo(self.alumno.dni, self.libro.isbn)
        self.alumno.prestamos.append(prestamo)
        self.prestamos.append(prestamo)
        self.assertEqual(self.libro.disponibles, 1)
        self.assertFalse(prestamo.devuelto)

        ya_prestado = any(
            p.alumno_dni == self.alumno.dni and p.libro_isbn == self.libro.isbn and not p.devuelto
            for p in self.prestamos
        )
        self.assertTrue(ya_prestado)

        prestamo.devolver()
        self.libro.devolver()
        self.assertTrue(prestamo.devuelto)
        self.assertEqual(self.libro.disponibles, 2)

    def test_agregar_y_eliminar_libro(self):
        self.assertIn("111", self.libros)
        del self.libros["111"]
        self.assertNotIn("111", self.libros)

    def test_agregar_y_eliminar_alumno(self):
        self.assertIn("22222222B", self.alumnos)
        del self.alumnos["22222222B"]
        self.assertNotIn("22222222B", self.alumnos)

if __name__ == '__main__':
    unittest.main()
