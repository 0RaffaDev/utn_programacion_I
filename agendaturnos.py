lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese nombre del operador: ")

while not operador.isalpha():
    operador = input("Nombre inválido. Ingrese nuevamente: ")

while True:
    print("\n--- AGENDA DE TURNOS ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        opcion = input("Opción inválida. Ingrese nuevamente: ")

    opcion = int(opcion)

    # RESERVAR TURNO
    if opcion == 1:

        print("\n1. Lunes")
        print("2. Martes")

        dia = input("Seleccione el día: ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Día inválido. Ingrese nuevamente: ")

        dia = int(dia)

        paciente = input("Ingrese nombre del paciente: ")

        while not paciente.isalpha():
            paciente = input("Nombre inválido. Ingrese nuevamente: ")

        if dia == 1:

            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("El paciente ya tiene un turno ese día.")

            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado correctamente.")

            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado correctamente.")

            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado correctamente.")

            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado correctamente.")

            else:
                print("No hay turnos disponibles para el lunes.")

        else:

            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("El paciente ya tiene un turno ese día.")

            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado correctamente.")

            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado correctamente.")

            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado correctamente.")

            else:
                print("No hay turnos disponibles para el martes.")

    # CANCELAR TURNO
    elif opcion == 2:

        print("\n1. Lunes")
        print("2. Martes")

        dia = input("Seleccione el día: ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Día inválido. Ingrese nuevamente: ")

        dia = int(dia)

        paciente = input("Ingrese nombre del paciente: ")

        while not paciente.isalpha():
            paciente = input("Nombre inválido. Ingrese nuevamente: ")

        if dia == 1:

            if paciente == lunes1:
                lunes1 = ""
                print("Turno cancelado correctamente.")

            elif paciente == lunes2:
                lunes2 = ""
                print("Turno cancelado correctamente.")

            elif paciente == lunes3:
                lunes3 = ""
                print("Turno cancelado correctamente.")

            elif paciente == lunes4:
                lunes4 = ""
                print("Turno cancelado correctamente.")

            else:
                print("No se encontró un turno para ese paciente.")

        else:

            if paciente == martes1:
                martes1 = ""
                print("Turno cancelado correctamente.")

            elif paciente == martes2:
                martes2 = ""
                print("Turno cancelado correctamente.")

            elif paciente == martes3:
                martes3 = ""
                print("Turno cancelado correctamente.")

            else:
                print("No se encontró un turno para ese paciente.")

    # VER AGENDA
    elif opcion == 3:

        print("\n1. Lunes")
        print("2. Martes")

        dia = input("Seleccione el día: ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Día inválido. Ingrese nuevamente: ")

        dia = int(dia)

        if dia == 1:

            print("\n--- AGENDA DEL LUNES ---")

            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", lunes1)

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", lunes2)

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", lunes3)

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print("Turno 4:", lunes4)

        else:

            print("\n--- AGENDA DEL MARTES ---")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", martes1)

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", martes2)

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", martes3)

    # RESUMEN GENERAL
    elif opcion == 4:

        ocupados_lunes = 0

        if lunes1 != "":
            ocupados_lunes += 1

        if lunes2 != "":
            ocupados_lunes += 1

        if lunes3 != "":
            ocupados_lunes += 1

        if lunes4 != "":
            ocupados_lunes += 1

        ocupados_martes = 0

        if martes1 != "":
            ocupados_martes += 1

        if martes2 != "":
            ocupados_martes += 1

        if martes3 != "":
            ocupados_martes += 1

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print("\n--- RESUMEN GENERAL ---")
        print("Lunes:", ocupados_lunes, "ocupados y", disponibles_lunes, "disponibles.")
        print("Martes:", ocupados_martes, "ocupados y", disponibles_martes, "disponibles.")

        if ocupados_lunes > ocupados_martes:
            print("El día con más turnos es Lunes.")

        elif ocupados_martes > ocupados_lunes:
            print("El día con más turnos es Martes.")

        else:
            print("Hay empate entre Lunes y Martes.")

    # CERRAR SISTEMA
    elif opcion == 5:

        print("\nSistema cerrado.")
        break