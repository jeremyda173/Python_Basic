#Condiciones

'''
Escribir una función que reciba una cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y
minúsculas.
'''

contraa = "contraseña"
contra2 = input("Introduce tu contraseña: ")
if contraa == contra2.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")