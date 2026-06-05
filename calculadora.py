def sumar():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    resultado = num1 + num2

    print(f"El resultado de {num1} + {num2} es: {resultado}")

def restar():
    num1=int(input("ingrese su primer numero: "))
    num2=int(input("Ingrese su segundo numero: "))
    print(f"El resultado de la resta es {num1-num2}")

def dividir():
    print("Dividir")
    a=float(input("Ingresa el primer numero: "))
    b=float(input("Ingresa el segundo numero: "))
    print(f"resultado: {a/b}")


def multiplicar():
    print("Multiplicar")

def potencia(a,  b):
    base = a
    for i in range(b -1):
        base *= a
    print(f"Resultado = {base}")
def raiz():
    print("Raiz")

def mod():
    print("MOD")
    try:
        num1=int(input("Ingrese el pimer número"))
        num2=int(input("Ingrese el sgundo número"))
        print(f"El resultado de {num1} mod {num2} es: {num1%num2}")
    except ValueError:
        print("Ingrese un valor numérico")

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
        opcion=int(input("Ingrse opcion a trabajar: "))

    except ValueError:
        print("debe ingresar un numero entero")
        continue

if opcion==1:
    sumar()
elif opcion==2:
    restar()
elif opcion==3:
    dividir()
elif opcion==4:
    multiplicar()
elif opcion==5:
    a = int(input("Ingresa la base"))
    b = int(input("Ingresa la potencia"))
    potencia(a,b)
elif opcion==6:
    raiz()
elif opcion==7:
    mod()
elif opcion==0:
    print(f"Salir de la fea calculadora")
    break
else:
    print("Opcion no encontrada")
    