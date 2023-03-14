#Ciclos

'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''

# Pedir al usuario un número entero
num = int(input("Introduzca un número entero: "))

# Imprimir un triángulo rectángulo descendente
for i in range(1, num+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()