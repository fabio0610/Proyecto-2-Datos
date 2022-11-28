from Tablero import Tablero
import copy
import random

class Juego():

    def __init__(self):
        self.nuevo_juego()

    def nuevo_juego(self):
        self.tablero = Tablero()

    def elige_ficha(self):
        simb = None
        while not simb:
            resp = input("Introduce el simbolo el simbolo para jugar 'X' o 'O' ? ")
            if resp.upper() == "X" or resp.upper() == "O":
                simb = resp.upper()
            else:
                print("Introduce una opcion valida!\n")
        if simb == "X":
            self.ficha1 = "X"
            self.ficha2 = "O"
        elif simb == "O":
            self.ficha1 = "O"
            self.ficha2 = "X"

    def jugada_humano(self, ficha):
        jugada = False
        while not jugada:
            if ficha == self.ficha1:
                print("Turno del jugador 1: ")
            else:
                print("Turno del jugador 2: ")
            fil = input("Introduce el numero de fila")
            col = input("Introduce el numero de columna")
            if self.tablero.casilla_vacia(fil, col) == True:
                self.tablero.tablero[int(fil)][int(col)] = ficha
                jugada = True
            else:
                print("Casilla ocupada, elije otra")
                print()

        print()

    def insertar_ficha(self, i, j, ficha):
        self.tablero.tablero[i][j] = ficha

    def eliminar_ficha(self, i, j):
        self.tablero.tablero[i][j] = " "

    def jugada_facil(self):
        print("Turno de la computadora")
        casilla = (random.choice(self.tablero.casillas_libres()))
        if self.tablero.hay_casillas_libres():
            self.insertar_ficha(casilla[0], casilla[1], self.ficha2)

    def jugada_dificil(self):
        print("Turno de la computadora")

    def partida_facil(self):

        self.elige_ficha()
        self.tablero.imprime()
        while not self.tablero.empate() and not self.tablero.gana():
            if not self.tablero.empate() and not self.tablero.gana():
                self.jugada_humano(self.ficha1)
                self.tablero.imprime()
                if self.tablero.gana(): print("HA GANADO EL JUGADOR 1")
            if not self.tablero.empate() and not self.tablero.gana():
                self.jugada_facil()
                self.tablero.imprime()
                if self.tablero.gana(): print("HA GANADO CPU")

        self.tablero.limpiaTablero()

    def partidaJvsJ(self):
        self.elige_ficha()
        self.tablero.imprime()
        while not self.tablero.empate() and not self.tablero.gana():
            if not self.tablero.empate() and not self.tablero.gana():
                self.jugada_humano(self.ficha1)
                self.tablero.imprime()
                if self.tablero.gana(): print("HA GANADO EL JUGADOR 1")

            if not self.tablero.empate() and not self.tablero.gana():
                self.jugada_humano(self.ficha2)
                self.tablero.imprime()
                if self.tablero.gana(): print("HA GANADO EL JUGADOR 2")

        if self.tablero.empate(): print("HAY UN EMPATE")
        self.tablero.limpiaTablero()

    def partida_intermedia(self):
        self.elige_ficha()
        self.tablero.imprime()
        while not self.tablero.empate() and not self.tablero.gana():
            if not self.tablero.empate() and not self.tablero.gana():
                self.jugada_humano(self.ficha1)
                self.tablero.imprime()
                if self.tablero.gana(): print("HA GANADO EL JUGADOR 1")
            if not self.tablero.empate() and not self.tablero.gana():
                self.jugada_intermedio()
                self.tablero.imprime()
                if self.tablero.gana(): print("HA GANADO CPU")

        self.tablero.limpiaTablero()

    def jugada_intermedio(self):
        print("Turno de la computadora")
        # Buscamos casillas para ganar
        tablero_aux = copy.deepcopy(self)
        lista_gane = self.tablero.casillas_libres()  # Lista de casillas libres

        for i in range(len(lista_gane)):
            casilla_gane = lista_gane[i]
            tablero_aux.insertar_ficha(casilla_gane[0], casilla_gane[1], tablero_aux.ficha2)
            if tablero_aux.tablero.gana():
                self.insertar_ficha(casilla_gane[0], casilla_gane[1], self.ficha2)
                return
            else:
                tablero_aux.eliminar_ficha(casilla_gane[0], casilla_gane[1])
        # Buscamos casillas para bloquear gane
        tablero_aux = copy.deepcopy(self)
        lista_bloqueo = self.tablero.casillas_libres()  # Lista de casillas libres
        for i in range(len(lista_bloqueo)):
            casillabloqueo = lista_bloqueo[i]
            tablero_aux.insertar_ficha(casillabloqueo[0], casillabloqueo[1], tablero_aux.ficha1)
            if tablero_aux.tablero.gana():
                self.insertar_ficha(casillabloqueo[0], casillabloqueo[1], self.ficha2)
                return
            else:
                tablero_aux.eliminar_ficha(casillabloqueo[0], casillabloqueo[1])

        # Si no hay opcion para ganar o bloquear se inserta la ficha en posicion al azar
        casilla = (random.choice(self.tablero.casillas_libres()))
        if self.tablero.hay_casillas_libres():
            self.insertar_ficha(casilla[0], casilla[1], self.ficha2)
        return
