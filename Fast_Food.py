opcion = '0'
total = 0


while opcion != '5':
    print('''
    1. Agregar Hamburguesa $4500.
    2. Agregar Papas Fritas $2000.
    3. Agregar Bebida $1500.
    4. Pagar pedido
    5. Cancelar pedido y salir
    ''')
    opcion = input('Ingrese una opcion: ')

    while not opcion.isdigit():
        print('Error. Ingrese una opcion valida')
        opcion = input('Ingrese una opcion: ')

    match opcion:
        case '1':
            total = total + 4500
            print('Hamburguesa agregada. Total actual: $', total)

        case '2':
            total = total + 2000
            print('Papas Fritas agregadas. Total actual: $', total)

        case '3':
            total = total + 1500
            print('Bebida agregada. Total actual: $', total)

        case '4':
            efect = input('Con cuanto efectivo abona? ')

            while not efect.isdigit():
                print('Error ingrese una cantidad valida.')
                efect = input('Con cuanto efectivo abona? ')

            efect = int(efect)

            while efect < total:
                print('Error. La cantidad de efectivo es menor al total.')
                
                efect = input('Con cuanto efectivo abona? ')

                while not efect.isdigit():
                    print('Error ingrese una cantidad valida.')
                    efect = input('Con cuanto efectivo abona? ')

                efect = int(efect)

            vuelto = efect - total
            print('Pago realizado. Vuelto a dar:', vuelto)

            total = 0                  
                            

        case '5':
            print('Saliendo...')
            break





