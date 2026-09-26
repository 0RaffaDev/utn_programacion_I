energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

racha_forzar = 0

nombre = input("Ingrese el nombre del agente: ")

while not nombre.isalpha():
    nombre = input("Nombre inválido. Ingrese nuevamente: ")

print("\nBienvenido, agente", nombre)
print("Tu misión es abrir las 3 cerraduras de la bóveda.")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:

    print("\n==============================")
    print("       ESTADO DE LA BÓVEDA")
    print("==============================")
    print("Agente:", nombre)
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Alarma:", alarma)
    print("Código parcial:", codigo_parcial)

    print("\n--- ACCIONES ---")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Opción inválida. Ingrese nuevamente: ")

    opcion = int(opcion)

    # FORZAR CERRADURA
    if opcion == 1:

        racha_forzar += 1

        energia -= 20
        tiempo -= 2

        print("\nIntentando forzar la cerradura...")

        # Regla anti-spam
        if racha_forzar == 3:

            print("¡La cerradura se trabó!")
            print("¡ALARMA ACTIVADA!")

            alarma = True

        else:

            # Riesgo de alarma si la energía es menor a 40
            if energia < 40:

                print("La energía está por debajo de 40.")
                print("Hay riesgo de activar la alarma.")

                numero = input("Ingrese un número del 1 al 3: ")

                while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                    numero = input("Número inválido. Ingrese un número del 1 al 3: ")

                numero = int(numero)

                if numero == 3:
                    alarma = True
                    print("¡ALARMA ACTIVADA!")

            if not alarma:

                cerraduras_abiertas += 1

                print("¡Cerradura abierta correctamente!")

    # HACKEAR PANEL
    elif opcion == 2:

        racha_forzar = 0

        energia -= 10
        tiempo -= 3

        print("\nIniciando hackeo del panel...")

        for paso in range(1, 5):

            print("Hackeando paso", paso, "de 4...")
            codigo_parcial += "A"

        print("Hackeo completado.")
        print("Código parcial:", codigo_parcial)

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:

            cerraduras_abiertas += 1

            print("¡El código es suficiente para abrir una cerradura!")
            print("¡Cerradura abierta!")

    # DESCANSAR
    elif opcion == 3:

        racha_forzar = 0

        energia += 15

        if energia > 100:
            energia = 100
            tiempo -= 1

        print("\nEl agente descansó.")
        print("Energía recuperada: +15")

        if alarma:

            energia -= 10

            print("La alarma está activa.")
            print("Se pierden 10 puntos de energía adicionales.")


# ==============================
# CONDICIONES FINALES
# ==============================

if cerraduras_abiertas == 3:

    print("\n==============================")
    print("         ¡VICTORIA!")
    print("==============================")
    print("Agente:", nombre)
    print("Abriste las 3 cerraduras.")
    print("¡La bóveda fue abierta!")

elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:

    print("\n==============================")
    print("      ¡DERROTA! BLOQUEO")
    print("==============================")
    print("La alarma bloqueó el sistema.")
    print("No lograste abrir la bóveda.")

elif energia <= 0:

    print("\n==============================")
    print("         ¡DERROTA!")
    print("==============================")
    print("Te quedaste sin energía.")

elif tiempo <= 0:

    print("\n==============================")
    print("         ¡DERROTA!")
    print("==============================")
    print("Se acabó el tiempo.")