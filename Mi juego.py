import time
import random
inicio = True
print("\n" + "Bienvenido al juego ESCAPA" + "\n" +
      "-" * len("Bienvenido al juego ESCAPA") + "\n")

print("""Tu y tu amigo los ha atrapado la policia, a tu amigo se lo llevaron
tu tienes la oportunidad de escapar, pero debes de ser rapido antes de que de atrapen, por donde te vas?\n""")

opcion = input("""\n[A] Te vas corriendo por la cuidad
[B] Vas por una entrada que viste
\nElije una opcion: """)

# El codigo de abajo es si el usuario elije A o a
if opcion == "A" or opcion == "a":
    print("\nTe vas corriendo por la cuidad y un policia te ve y te esta persiguiendo, que haces?\n")
    opcion = input("""\n[A] Te escondes
[B] Vas por una puerta que viste 
\nElije una opcion: """)

    if opcion == "A" or opcion == "a":
        print("\nTe descubre el policia y te atrapa\nFIN\n")
    elif opcion == "B" or opcion == "b":
        print("\nEntrastes en la puerta, todo se ve muy solo, sigues avanzando y te encuentras a una tortuga mutante y te puede ayudar, aceptas esta ayuda?\n")
        opcion = input("""\n[A] Aceptas la ayuda
[B] No la aceptas
\nElije una opcion: """)

        if opcion == "A" or opcion == "a":
            print("\nAceptaste la ayuda y te da algo de comer, y te pregunta si quieres ir por la derecha o izquierda\n")
            opcion = input("""\n[A] Derecha
[B] Izquierda
\nElije una opcion: """)

            if opcion == "A" or opcion == "a":
                print("\nVamos hacia la derecha, en un lugar con muy poca luz, pero se ve luz al final del camino, Quieres seguir caminando?\n")
                opcion = input("""\n[A] Seguiremos con el camino, sin importar lo que haya a lo ultimo
[B] Prefieres mejor irte por otro camino que viste durente el trayectorio pero no hay nada de luz
\nElije una opcion: """)
                if opcion == "A" or opcion == "a":
                    print(
                        "\nUps, esa luz era de un carro de policia que estaba vigilando la zona, Has perdido D:\n")
                    exit()
                elif opcion == "B" or opcion == "b":
                    print(
                        "\nEntraste a el camino para salir de la cuidad, La tortuga antes de poder irte te pregunta algo, ...")
                    numero_tortuga = random.randint(1, 10)
                print("\nLa tortuga te pregunta el resultado de esta operacion, la debes contestar para escapar de los policias: 2 * {}".format(numero_tortuga))
                opcion = int(input("\nCual es el resultado?:"))
                if opcion == 13 * numero_tortuga:
                    print("\nNo eres digno para escapar\nFIN")
                    exit()
                else:
                    print(
                        "\nEres digno para salir de la cuidad y escapar\n HAS GANADO :D\n")
                    opcion = input("Quieres salir? S/N: ")
                    while inicio:
                        if opcion == "S" or opcion == "s":
                            exit()
                        elif opcion == "N" or opcion == "n":
                            inicio = True
        elif opcion == "B" or opcion == "b":
            print("\nTe Mata por que fuiste un mal agradecido\n")
            exit()
# El codigo de abajo es si el usuario elije B o b
elif opcion == "B" or opcion == "b":
    print("\nEntraste a la entrada, este lugar tiene muchas ventanas y ves a lo lejos a tu companero sufriendo, pero no puedes hacer mucho ruido o si no acabaras como el\n")
    opcion = input("""\n[A] Te quedas llorando 
[B] Sigues tu camino, pero estas muy triste
\nElije una opcion: """)
    if opcion == "A" or opcion == "a":
        print("\nHas hecho mucho ruido y llegaron los policias por ti, Has perdido\n")
        exit()
    elif opcion == "B" or opcion == "b":
        print("seguiras el camino, ves a una mariposa magica a lo lejos, quieres seguir o tomar otro camino?")
        opcion = input("""\n[A] Sigues pero con el riesgo que la mariposa te mate
[B] Tomo otro camino
\nElije una opcion: """)
        if opcion == "A" or opcion == "a":
            print("\nTe da una guia de como salir de la cuidad y perder a la policia, a cambio de que le digas el maximo de estos numeros: \n")
            opcion1 = input("""\n[A] 123411
[B] 123419
\nCual es el maximo: """)
            if opcion1 == "A" or opcion1 == "a":
                print("\nIncorrecto, Has perdido\n")
            elif opcion1 == "B" or opcion1 == "b":
                print(
                    "\nEl camino es mas hacia delante, para poder salir de los policias, corre para ganar!!!!\n")
                time.sleep(2)
                print("\nHas ganado :DD\n")
                opcion = input("Quieres salir? S/N: ")
                while inicio:
                    if opcion == "S" or opcion == "s":
                            exit()
                    elif opcion == "N" or opcion == "n":
                            inicio = True