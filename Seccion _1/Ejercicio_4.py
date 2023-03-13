#Uso de cadenas y strings

'''
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extensión
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo
+34-913724710-56). Escribir una función que reciba número de teléfono con este
formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
'''

telefono = input("Insertar un numero de con el formato +aa-aaaaaaaaa-aa: ")
print("El numero es", telefono[4:-3])
print("El codigo de pais es", telefono[0:-13])