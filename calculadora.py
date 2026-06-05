def sumar():
    print("sumar")

def restar():
    print("Restar")

def dividir():
    print("Dividir")

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