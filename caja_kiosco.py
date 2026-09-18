print('---Caja Kiosco---')
# Nombre del cliente
nombre = input("Nombre del cliente: ")

while nombre == "" or not nombre.isalpha():
    print("Nombre inválido.")
    nombre = input("Nombre del cliente: ")


# Cantidad de productos
cantidad = input("Cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Cantidad inválida.")
    cantidad = input("Cantidad de productos: ")

cantidad = int(cantidad)


total_sin_descuentos = 0
total_con_descuentos = 0


# Productos
for i in range(cantidad):
    precio = input(f"Producto {i + 1} - Precio: ")

    while not precio.isdigit():
        print("Precio inválido.")
        precio = input(f"Producto {i + 1} - Precio: ")

    precio = int(precio)

    descuento = input("Descuento (S/N): ").lower()

    while descuento != "s" and descuento != "n":
        print("Debe ingresar S o N.")
        descuento = input("Descuento (S/N): ").lower()

    total_sin_descuentos += precio

    if descuento == "s":
        precio = precio * 0.90

    total_con_descuentos += precio


# Resultados
ahorro = total_sin_descuentos - total_con_descuentos
promedio = float(total_con_descuentos) / cantidad

print()
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")