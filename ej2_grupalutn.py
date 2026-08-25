ventas = []
opcion = 0
total = 0
contador = 0

while opcion != '5':
    print('''===== KIOSCO - GESTION DE VENTAS =====
    1. Registrar venta
    2. Ver listado de ventas del turno
    3. Ver total recaudado
    4. Buscar ventas de un producto
    5. Cerrar caja y salir
    ''')

    opcion = input("Elija una opcion: ")

    match opcion:
        case '1':
            producto = input('Ingrese el nombre del producto: ')

            precio = float(input('Ingrese el precio unitario: '))
            while precio <= 0:
                print("El precio debe ser un valor positivo.")
                precio = float(input('Ingrese el precio unitario: '))

            cantidad = int(input('Ingrese la cantidad de productos: '))
            while cantidad <= 0:
                print("La cantidad debe ser un valor positivo.")
                cantidad = int(input('Ingrese la cantidad de productos: '))

            subtotal = precio * cantidad

            if subtotal > 10000:
                subtotal = subtotal * 0.90

            venta = {
                'producto': producto,
                'precio': precio,
                'cantidad': cantidad,
                'subtotal': subtotal
            }

            ventas.append(venta)
            print('Venta agregada con exito!')

        case '2':
            for venta in ventas:
                print("Producto:", venta['producto'])
                print("Precio:", venta['precio'])
                print("Cantidad:", venta['cantidad'])
                print("Subtotal:", venta['subtotal'])
                print("--------------------")

        case '3':
            total = 0

            for venta in ventas:
                total = total + venta["subtotal"]

            print("Total recaudado: ", total)

        case '4':
            producto_buscar = input("Ingrese el nombre del producto que desea buscar: ")
            unidades_totales = 0
            
            for venta in ventas:
                 if venta['producto'].lower() == producto_buscar.lower():
                    unidades_totales = unidades_totales + venta['cantidad']
            
            print("Unidades vendidas de", producto_buscar, ":", unidades_totales)
            

        case '5':
              print("Cerrando gestion de ventas... Adios!")
              break
      

        case _:
            print("Opcion invalida. Ingrese una opcion del 1 al 5.")