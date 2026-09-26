print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")


# ESTADÍSTICAS INICIALES

vida_jugador = 100
vida_enemigo = 100
pociones = 3

ataque_pesado = 15
danio_enemigo = 12

turno_gladiador = True


print("\n=== INICIO DEL COMBATE ===")


# CICLO DE COMBATE

while vida_jugador > 0 and vida_enemigo > 0:

    if turno_gladiador:

        print("\n--------------------------------")
        print(nombre, "(HP:", vida_jugador, ")")
        print("Enemigo (HP:", vida_enemigo, ")")
        print("Pociones:", pociones)
        print("--------------------------------")

        print("\nElige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        # ATAQUE PESADO
        if opcion == 1:

            if vida_enemigo < 20:

                danio = ataque_pesado * 1.5

                vida_enemigo -= danio

                print("\n¡Golpe Crítico!")
                print("¡Atacaste al enemigo por", danio, "puntos de daño!")

            else:

                danio = ataque_pesado

                vida_enemigo -= danio

                print("\n¡Atacaste al enemigo por", danio, "puntos de daño!")

        # RÁFAGA VELOZ
        elif opcion == 2:

            print("\n>> ¡Inicias una ráfaga de golpes!")

            for golpe in range(3):

                vida_enemigo -= 5

                print("> Golpe conectado por 5 de daño")

        # CURAR
        elif opcion == 3:

            if pociones > 0:

                vida_jugador += 30

                if vida_jugador > 100:
                    vida_jugador = 100
                    pociones -= 1

                print("\n¡Usaste una poción!")
                print("Recuperaste 30 puntos de vida.")
                print("Vida actual:", vida_jugador)

            else:

                print("\n¡No quedan pociones!")

        # CAMBIO DE TURNO
        turno_gladiador = False


    # TURNO DEL ENEMIGO
    else:

        if vida_enemigo > 0 and vida_jugador > 0:

            vida_jugador -= danio_enemigo

            print("\n>> ¡El enemigo contraataca por", danio_enemigo, "puntos!")

        turno_gladiador = True

        print("\n=== NUEVO TURNO ===")


# FIN DEL JUEGO

print("\n================================")

if vida_jugador > 0:

    print("¡VICTORIA!", nombre, "ha ganado la batalla.")

else:

    print("DERROTA. Has caído en combate.")

print("================================")