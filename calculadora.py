def sumar():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    resultado = num1 + num2

    print(f"El resultado de {num1} + {num2} es: {resultado}")

def restar():
    num1 = int(input("ingrese su primer numero: "))
    num2 = int(input("Ingrese su segundo numero: "))
    print(f"El resultado de la resta es {num1-num2}")

def dividir():
    print("Dividir")
    a = float(input("Ingresa el primer numero: "))
    b = float(input("Ingresa el segundo numero: "))
    print(f"resultado: {a / b}")


def multiplicar():
    print("Multiplicar")

def potencia():
    a = int(input("Ingresa la base "))
    b = int(input("Ingresa la potencia "))
    base = a
    for i in range(b - 1):
        base *= a
    print(f"Resultado = {base}")
def raiz():
    print("Raiz")

def mod():
    print("MOD")
    try:
        num1 = int(input("Ingrese el pimer número"))
        num2 = int(input("Ingrese el sgundo número"))
        print(f"El resultado de {num1} mod {num2} es: {num1%num2}")
    except ValueError:
        print("Ingrese un valor numérico")

def salir():
    print(f"Salir de la fea calculadora")

def main():
    while True:
        try:
            print("bienvenido a la calculadora mas completa y epica de la historia")
            print("1) Sumar")
            print("2) Restar")
            print("3) Dividir")
            print("4) Multiplicar")
            print("5) Potencia")
            print("6) Raiz")
            print("7) MOD")
            print("0) Salir")
            opcion = int(input("Ingrese opcion a trabajar: "))

        except ValueError:
            print("debe ingresar un numero entero")
            continue

        match opcion:
            case 1:
                sumar()
            case 2:
                restar()
            case 3:
                dividir()
            case 4:
                multiplicar()
            case 5:
                potencia()
            case 6:
                raiz()
            case 7:
                mod()
            case 0:
                salir()
                break
            case _:
                print("Opcion no encontrada")

main()