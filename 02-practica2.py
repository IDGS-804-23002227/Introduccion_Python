'''
Crear un programa que permita realizar las operaciones basicas +, -, *, /
utilizando una funcion para cada operacion  y un menu principal para desplegar y elegir que operacion realizaremos

'''    

def suma():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print("Resultado: ", a + b)
    
def resta():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print("Resultado: ", a - b)
    
def multiplicacion():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print ("Resultado: ",a * b)

def division():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    
    if b==0:
        print("No se puede dividir")
    else:
        print("Resultado: ", a / b)

def menu():
    print("1. Opción sumar")
    print("2. Opción restar")
    print("3. Opción multiplicar")
    print("4. Opción dividir")
    print("5. Opción salir")
    
    opcion = int(input("Elige una opcion: "))
    return opcion

def main():
    opcion = 0
    
    while opcion != 5:
        opcion = menu()
        
        if opcion == 1:
            suma()
        
        elif opcion == 2:
            resta()
        
        elif opcion == 3:
            multiplicacion()
            
        elif opcion == 4:
            division()
        
        elif opcion == 5:
            print("Salir.")
        
        else:
            print("Opcion no valida.")
    
if __name__ == "__main__":
    main()


            
        
            
        
        
        
        
        
            
        
        
    
    
    
