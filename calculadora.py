def sumar():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    resultado = num1 + num2

    print(f"El resultado de {num1} + {num2} es: {resultado}")

def restar():
    print("Restar")

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

print("Welcome to my calculator")
print("1) Sumar")
print("2) Restar")
print("3) Dividir")
print("4) Multiplicar")
print("5) Potencia")
print("6) Raiz")
print("7) MOD")
print("0) Salir")
opcion=int(input("Ingrse opcion a trabajar"))

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
    print(f"Salir de la hermosa calculadora")
else:
    print("Opcion no encontrada")