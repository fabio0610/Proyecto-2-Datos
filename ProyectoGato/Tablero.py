import random
import types
import copy
import os




class Tablero():
    def __init__(self):
        self.ficha1 = " "
        self.ficha2 = " "
        self.tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def casillas_libres(self):
        """
        Regresa una lista con todas las casillas libres
        """
        return [(i, j) for j in random.sample(range(3), 3)
                for i in random.sample(range(3), 3)
                if self.casilla_vacia(i, j)]

    def limpiaTablero(self):
        self.tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def empate(self):
        if not self.gana() and not self.hay_casillas_libres():
            return True
        return False

    def gana(self):
        for i in range(3):
            horizontal = [self.tablero[i][j] for j in range(3)]
            if horizontal.count("X") == 3 or horizontal.count("O") == 3:
                return True

        for i in range(3):
            vertical = [self.tablero[j][i] for j in range(3)]
            if vertical.count("X") == 3 or vertical.count("O") == 3:
                return True

        diagonal1 = [self.tablero[i][i] for i in range(3)]
        if diagonal1.count("X") == 3 or diagonal1.count("O") == 3:
            return True
        diagonal2 = [self.tablero[2 - i][i] for i in range(3)]
        if diagonal2.count("X") == 3 or diagonal2.count("O") == 3:
            return True

        return False

    def hay_casillas_libres(self):
        if len(self.casillas_libres()) > 0:
            return True
        else:
            return False

    def imprime(self):
        """
        Imprime el tablero
        """
        print(" ", self.tablero[0][0], "|", self.tablero[0][1], "|", self.tablero[0][2])
        print("----+---+----")
        print(" ", self.tablero[1][0], "|", self.tablero[1][1], "|", self.tablero[1][2])
        print("----+---+----")
        print(" ", self.tablero[2][0], "|", self.tablero[2][1], "|", self.tablero[2][2])

    def casilla_vacia(self, fila, col):
        return True if self.tablero[int(fila)][int(col)] == " " else False