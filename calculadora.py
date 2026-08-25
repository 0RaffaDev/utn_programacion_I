def sumar(num1,num2):
    total = num1 + num2 
    return total

def resta(num1,num2):
    total = num1 - num2
    return total

def multiplicar(num1, num2):
    total = num1 * num2
    return total

def dividir(num1, num2):
    if num2 == 0:
        return "No se puede dividir por 0"
    
    total = num1 / num2
    return total
opcion = 0
while opcion != '5':
    print('===== CALCULADORA  =====')
    print('''
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir
    ''')
    opcion = input('Ingrese una opcion:')
    match opcion:
        case '1':
            num1 = float(input('Ingrese numero 1 a sumar: '))
            num2 = float(input('Ingrese numero 2 a sumar: '))
            print('El resultado es: ', sumar(num1,num2))

        case '2':
            num1 = float(input('Ingrese numero 1 a restar: '))
            num2 = float(input('Ingrese numero 2 a restar: '))
            print('El resultado es: ', resta(num1,num2))
        case '3':
            num1 = float(input('Ingrese numero 1 a multiplicar: '))
            num2 = float(input('Ingrese numero 2 a multiplicar: '))
            print('El resultado es: ', multiplicar(num1,num2))
        case '4':
            num1 = float(input('Ingrese numero 1 a dividir: '))
            num2 = float(input('Ingrese numero 2 a dividir: '))
            print('El resultado es: ', dividir(num1,num2))
        case '5':
            break
        case _:
            print('Ingrese una opcion valida')
        
