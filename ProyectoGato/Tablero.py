import random
import types
import copy
import os




class Tablero():
    def __init__(self):
        """
        Se crea el constructor que permite la elaboración del tablero del juego Gato
        """

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
        """
        La función se encarga de dejar el tablero vacío
        """
        self.tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def empate(self):
        """
        Se realiza una verificación de que el tablero resulte en un empate
        """
        if not self.gana() and not self.hay_casillas_libres():
            return True
        return False

    def gana(self):
        """
        En esta función se verifica en cada caso que se puede dar para que un jugador pueda declararse ganador y dicha
        función se retornara verdadero en caso de cumplirse una condición o falso en caso de ninguna
        """
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
        """
        Se da una simple verificación de que hayan casillas libres en la totalidad el tablero
        """
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
        """
        Verificacion de una casilla vacia en específico
        """
        return True if self.tablero[int(fila)][int(col)] == " " else False