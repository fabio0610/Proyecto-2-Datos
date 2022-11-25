from Tablero import Tablero
import copy
import random
class Gato():

    def __init__(self):
        self.nuevo_juego()

    def nuevo_juego(self):
        self.termina_juego = False  # Por default el juego no ha terminado
        self.mensaje_inicial()
        self.tablero = Tablero()
        self.humano_elige_simbolo()

    def mensaje_inicial(self):
        print("""
        Juego de gato
        -------------
        """)

    def humano_elige_simbolo(self):
        simb = None
        while not simb:
            resp = input("Humano quieres jugar con 'x' o 'o' ? ")
            if resp.lower() == "x" or resp.lower() == "o":
                simb = resp.lower()
            else:
                print("Elección incorrecta, intenta de nuevo!\n")
        self.tablero.elijir(simb)

    def imprime_resultado(self, turno):

        self.tablero.imprimir()

        if self.tablero.gana(turno):
            print("""
            El ganador es {}
            """.format("el Humano" if turno == 1 else "la IA"))
        else:
            print("""
            El juego es un empate!
            """)

    def otro_juego(self):
        print()
        valida = False
        while not valida:
            resp = input("Desea realizar otro juego? (Si/No)")
            if resp.lower() in ["si", "s", "no", "n"]:
                valida = True
                resp = resp.lower()
            else:
                print("Respuesta incorrecta, intente de nuevo!\n")
        if resp in ["si", "s"]:
            self.nuevo_juego()
        else:
            self.termina_juego = True

    def run(self):

        while not self.termina_juego:
            turno = random.choice([-1, 1])  # Se elige quien inicia el juego al azar
            while not self.tablero.empate() and not self.tablero.gana(turno):
                self.tablero.imprimir()
                if turno == 1:
                    self.tablero.juega_humano()
                    if self.tablero.gana(turno):
                        continue
                    turno = -1
                else:
                    self.tablero.juega_ia()
                    if self.tablero.gana(turno):
                        continue
                    turno = 1
            self.imprime_resultado(turno)
            self.otro_juego()


# Se crea una instancia del juego
gato = Gato()

# Se inicia el juego
gato.run()