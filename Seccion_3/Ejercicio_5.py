#Ciclos

'''
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a
una las letras de la palabra introducida empezando por la última.
'''

# Pedir al usuario una palabra
palabra = input("Introduzca una palabra: ")

# Imprimir las letras de la palabra en orden inverso
for letra in reversed(palabra):
    print(letra)