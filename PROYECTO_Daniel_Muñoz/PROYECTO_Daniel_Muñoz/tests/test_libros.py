import unittest
from models.libro import Libro

class TestLibro(unittest.TestCase):
    def test_creacion_libro(self):
        libro = Libro("123", "El Quijote", "Cervantes", "2ESO", 5)
        self.assertEqual(libro.isbn, "123")
        self.assertEqual(libro.titulo, "El Quijote")
        self.assertEqual(libro.autor, "Cervantes")
        self.assertEqual(libro.curso, "2ESO")
        self.assertEqual(libro.ejemplares, 5)
        self.assertEqual(libro.disponibles, 5)

    def test_prestar_y_devolver(self):
        libro = Libro("123", "El Quijote", "Cervantes", "2ESO", 2)
        self.assertTrue(libro.prestar())
        self.assertEqual(libro.disponibles, 1)
        self.assertTrue(libro.prestar())
        self.assertEqual(libro.disponibles, 0)
        self.assertFalse(libro.prestar())
        self.assertTrue(libro.devolver())
        self.assertEqual(libro.disponibles, 1)
        self.assertTrue(libro.devolver())
        self.assertEqual(libro.disponibles, 2)
        self.assertFalse(libro.devolver())

if __name__ == '__main__':
    unittest.main()
