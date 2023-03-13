#Uso de cadenas y strings

'''
Escribir una función que reciba el nombre del usuario y un número entero e imprima por
pantalla en líneas distintas el nombre del usuario tantas veces como el número
introducido.
'''

nombre = input("¿Cúal es tú nombre? ")
l = input("Escribe un número entero: ")
print((nombre + "\n") * int(l))
