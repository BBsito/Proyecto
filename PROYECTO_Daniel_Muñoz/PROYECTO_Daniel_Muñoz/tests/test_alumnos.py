import unittest
from models.alumno import Alumno

class TestAlumno(unittest.TestCase):
    def test_creacion_alumno(self):
        alumno = Alumno("12345678A", "Daniel Muñoz", "1DAW")
        self.assertEqual(alumno.dni, "12345678A")
        self.assertEqual(alumno.nombre, "Daniel Muñoz")
        self.assertEqual(alumno.curso, "1DAW")
        self.assertIsInstance(alumno.prestamos, list)
        self.assertEqual(len(alumno.prestamos), 0)

    def test_to_dict_and_from_dict(self):
        alumno = Alumno("23456789A", "Lorena Muñoz", "2ESO")
        d = alumno.to_dict()
        self.assertEqual(d, {
            "dni": "23456789A",
            "nombre": "Lorena Muñoz",
            "curso": "2ESO"
        })
        alumno2 = Alumno.from_dict(d)
        self.assertEqual(alumno2.dni, "23456789A")
        self.assertEqual(alumno2.nombre, "Lorena Muñoz")
        self.assertEqual(alumno2.curso, "2ESO")

if __name__ == '__main__':
    unittest.main()
