#Uso de cadenas y strings

'''
Escribir una función que reciba el nombre del usuario y después muestre por pantalla
<NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en
mayúsculas y <n> es el número de letras que tienen el nombre.
'''

nombre = input("¿Cúal es tú nombre? ")
print("Sabias que " + nombre.upper() + " tiene " + str(len(nombre)) + " letras")