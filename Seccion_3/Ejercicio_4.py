#Ciclos

'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase.
'''

# Pedir al usuario una frase y una letra
frase = input("Introduzca una frase: ")
letra = input("Introduzca una letra: ")

# Contar el número de veces que aparece la letra en la frase
contador = 0
for caracter in frase:
    if caracter == letra:
        contador += 1

# Mostrar el resultado
print("La letra", letra, "aparece", contador, "veces en la frase.")