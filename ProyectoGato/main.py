from Juego import Juego



print("Bienvenido al juego de gato")
print("\n\n\nElija una de las siguientes opciones: ")
print("\n")

def menu_principal():
    print("1) Jugador vs Jugador")
    print("2) Jugador vs CPU")
    print("3) Salir")

def menu_CPU():
    print("Elija una dificultad: ")
    print("1) Facil")
    print("2) Normal")
    print("3) Dificil")
    print("4) Volver")





while (True):
    print("\n\n")
    menu_principal()
    opcion = input("Ingrese una opcion: ")
    if (opcion == "1"):
        Juego().partidaJvsJ()
    elif (opcion == "2"):
        print("\n\n")
        while (True):
            menu_CPU()
            opcion = input("Ingrese una opcion: ")
            if(opcion == "1"):
                Juego().partida_facil()
            elif (opcion == "2"):
                Juego().partida_intermedia()
            elif (opcion == "3"):
                Juego().partida_dificil()
            elif (opcion == "4"):
                break
            else:
                print("Opcion incorrecta, imgrese una opcion valida ")
                print("\n\n")

    elif (opcion == "3"):
        break
    else:

        print("Opcion incorrecta, imgrese una opcion valida ")
        print("\n\n")

