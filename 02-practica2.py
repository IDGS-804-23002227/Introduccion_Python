'''
Crear un programa que permita realizar las operaciones basicas +, -, *, /
itulizando una fincion para cada operacion  y un menu principal para desplegar y elegir que operacion realizaremos

'''

def suma():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print("Resultado:", a + b)
    
def resta():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print("Resultado: ", a - b)
    
def multiplicacion():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    ("Resultado: ", a * b)

def division():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    ("Resultado: ", a / b)