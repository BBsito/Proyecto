import unittest
from models.prestamo import Prestamo
from datetime import date

class TestPrestamo(unittest.TestCase):
    def test_creacion_prestamo(self):
        p = Prestamo(alumno_dni="12345678A", libro_isbn="987654321")
        self.assertEqual(p.alumno_dni, "12345678A")
        self.assertEqual(p.libro_isbn, "987654321")
        self.assertFalse(p.devuelto)
        self.assertIsNone(p.fecha_devolucion)
        self.assertEqual(p.fecha_prestamo, date.today().isoformat())

    def test_devolver(self):
        p = Prestamo(alumno_dni="12345678A", libro_isbn="987654321")
        p.devolver()
        self.assertTrue(p.devuelto)
        self.assertEqual(p.fecha_devolucion, date.today().isoformat())

    def test_to_dict_and_from_dict(self):
        p = Prestamo(alumno_dni="12345678A", libro_isbn="987654321", fecha_prestamo="2025-01-01", devuelto=True, fecha_devolucion="2025-01-15")
        d = p.to_dict()
        self.assertEqual(d['alumno_dni'], "12345678A")
        self.assertEqual(d['libro_isbn'], "987654321")
        self.assertEqual(d['fecha_prestamo'], "2025-01-01")
        self.assertTrue(d['devuelto'])
        self.assertEqual(d['fecha_devolucion'], "2025-01-15")
        p2 = Prestamo.from_dict(d)
        self.assertEqual(p2.alumno_dni, "12345678A")
        self.assertEqual(p2.libro_isbn, "987654321")
        self.assertEqual(p2.fecha_prestamo, "2025-01-01")
        self.assertTrue(p2.devuelto)
        self.assertEqual(p2.fecha_devolucion, "2025-01-15")

if __name__ == '__main__':
    unittest.main()
