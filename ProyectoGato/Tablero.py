import copy
import random


# Se crea una clase en la que se realizará el desarrollo del tablero del gato
class Tablero():
    def __init__(self): # Se declara el tablero a utilizar
        self.tablero = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def poner_libres(self): # Devuelve una lista de true or false indicando que espacios estan libres
        cas_libre = [(i, j) for j in random.sample(range(3), 3)
                for i in random.sample(range(3), 3)
                if self.es_vacia((i, j))]
        return cas_libre

    def empate(self): # que el juego sea un empate
        if self.poner_libres():
            ver = False
        else:
            ver = True
        return ver

    def gana(self, jugador): # Se crea uan función que verifique que algun jugador gane
        verificacion = False
        # Se busca en horizontales
        for ren in self.tablero:
            if abs(sum(ren)) == 3 and jugador in ren:
                verificacion = True
        # Se busca en verticales
        for col in zip(*self.tablero):
            if abs(sum(col)) == 3 and jugador in col:
                verificacion =  True
        # Se busca en diagonales
        diag1 = [self.tablero[i][i] for i in range(3)]
        if abs(sum(diag1)) == 3 and jugador in diag1:
            verificacion = True
        diag2 = [self.tablero[2 - i][i] for i in range(3)]
        if abs(sum(diag2)) == 3 and jugador in diag2:
            verificacion = True

        return verificacion

    def elijir(self, simb): #funcion que permite que se elija ente "x" o "o"
        if simb == "x":
            self.simbolos = [".", "x", "o"]
        else:
            self.simbolos = [".", "o", "x"]

    def imprimir(self):
        print()
        print("Tablero: ")
        print("  0 1 2")
        for i, linea in enumerate(self.tablero):
            print("{} {} {} {}".format(
                str(i), *[self.simbolos[v] for v in linea]))


    def jugada(self, p, j):
        self.tablero[p[0]][p[1]] = j

    def casilla_vacia(self, p):
        return True if self.tablero[p[0]][p[1]] == 0 else False

    def esquina(self, p):
        return True if p[0] in [0, 2] and p[1] in [0, 2] else False

    def juega_humano(self):
        print("Es tu turno humano!")
        tirada = False
        while not tirada:
            resp = input("Elije una casilla (ren, col)? ")
            p = [int(v) for v in resp.split(",")]
            if self.casilla_vacia(p):
                self.jugada(p, 1)
                tirada = True
            else:
                print("Casilla ocupada, elije otra!")
                print()

    def juega_ia(self):

        print("Turno de la IA!")
        # Se buscan las casillas disponibles de forma aleatoria
        casillas = self.poner_libres()
        # Se busca si la IA puede ganar en la siguiente tirada
        for c in casillas:
            tablero2 = copy.deepcopy(self)
            tablero2.jugada(c, -1)
            if tablero2.gana(-1):
                self.jugada(c, -1)
                return

        # Se busca si el Humano puede ganar en la siguiente tirada, si
        # es así hay que bloquearlo
        for c in casillas:
            tablero2 = copy.deepcopy(self)
            tablero2.jugada(c, 1)
            if tablero2.gana(1):
                self.jugada(c, -1)
                return

        # Ahora la estrategía es tirar en el esquinas, centro o lados,
        # en ese orden.
        esquinas = [c for c in casillas if self.esquina(c)]
        if esquinas:
            self.jugada(esquinas[0], -1)
            return

        casillas = [c for c in casillas if c not in esquinas]
        if (1, 1) in casillas:
            self.jugada((1, 1), -1)
            return

        casillas = [c for c in casillas if c != (1, 1)]
        if casillas:
            seld.haz_tirada(casillas[0], -1)
            return
