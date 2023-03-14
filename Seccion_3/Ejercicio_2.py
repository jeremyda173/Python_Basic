#Ciclos

'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****
'''

# Pedir al usuario un número entero
num = int(input("Introduzca un número entero: "))

# Imprimir un triángulo rectángulo de altura num
for i in range(1, num+1):
    print("*" * i)