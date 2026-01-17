'''
operacion de multiplicacion de a x b utilizando sumas 
a = 3
b = 4
salida : 3+3+3+3=12
'''

a = 3
b = 4

contador = 0
resultado = 0
tem = ""

while contador < b:
    resultado += a
    tem += str(a)
    if contador < b - 1:
        tem += "+"
    contador += 1

print(tem)
print(resultado)



        
    
    
    
