saldo = 50000
opcion = '0'

#Menu
while opcion != '4':
    print('''

    1. Consultar Saldo
    2. Ingresar Saldo
    3. Retirar Dinero
    4. Salir


    ''')
    opcion = input("Ingrese su opcion: ")


    #Funciones Menu
    match opcion:

        case '1':
            print('Su saldo es: ', saldo )
        case '2':
            ingreso = input("Cuanto dinero desea ingresar?: ")

            while not ingreso.isdigit():
                print("Error. Ingrese una cantidad valida")
                ingreso = input("Cuanto dinero desea ingresar? ")

            ingreso = int(ingreso)
            saldo = saldo + ingreso
            print("Su nuevo saldo es: ", saldo)

        case '3':
            retiro = input('Cuanto dinero desea retirar? ')

            while not retiro.isdigit():
                print("Error. Ingrese una cantidad valida")
                retiro = input("Cuanto dinero desea retirar?")

            retiro = int(retiro)
            saldo = saldo - retiro
            print("Su nuevo saldo es: ", saldo)

        case '4':
            print('Saliendo...')
            break




