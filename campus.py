import random

usuario = 'alumno'
clave = 'python123'
acceso = False

frases = [
    "¡Cada día estás un poco más cerca!",
    "¡No te rindas, seguí adelante!",
    "¡Todo esfuerzo tiene su recompensa!",
    "¡Vos podés lograrlo!"
]

for intento in range(1,4):
    print(f"Intento {intento}/3")
    us = input("Ingrese su usuario: ")
    ps = input("Ingrese su contraseña: ")


    if us == usuario and ps == clave:
        print("Acceso Correcto")
        print("Bienvenido Alumno!")
        acceso = True
        break
    else:
        print("Usuario o Contraseña Incorrecta.")
if acceso == False:
    print("Cuenta bloqueada. Intentelo de nuevo mas tarde.")

while acceso == True:
    print('''1. Ver estado de inscripcion.
    2. Cambiar Clave
    3. Mostrar mensaje motivacional
    4. Salir''')


    while True:
        opcion = input("Opción: ")

        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue
        break

    match opcion:
        case 1:
            print('Inscripto.')
        case 2:
            nueva_clave = input("Nueva clave: ")
            while len(nueva_clave) < 6:
                print("Error: la clave debe tener mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")

            confirmacion = input("Confirmar clave: ")

            if nueva_clave == confirmacion:
                clave_correcta = nueva_clave
                print("Clave cambiada correctamente.")
            else:
                print("Error: las claves no coinciden.")
                        
        case 3:
            print(random.choice(frases))
        case 4:
            print("Saliendo...")
            acceso = False

        

    




