def sumar():
    print("sumar")

def restar():

def dividir():
    print("Dividir")

def multiplicar():
    print("Multiplicar")

def potencia():
    print("Potencia")

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
    potencia()
elif opcion==6:
    raiz()
elif opcion==7:
    mod()
elif opcion==0:
    print(f"Salir de la fea calculadora")
    break
else:
    print("Opcion no encontrada")
    