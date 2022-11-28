import unittest
from Tablero import Tablero


class TestTablero(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Tablero().casilla_vacia(1,1), True)  # add assertion here
        self.assertEqual(Tablero().empate(), False)
        self.assertEqual(Tablero().gana(), False)


if __name__ == '__main__':
    unittest.main()
