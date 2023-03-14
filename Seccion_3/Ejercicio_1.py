#Ciclos

'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión cada año
que dura la inversión.
'''

# Pedir al usuario los datos de entrada
inversion = float(input("Introduzca la cantidad a invertir: "))
interes_anual = float(input("Introduzca el interés anual: "))
num_anios = int(input("Introduzca el número de años de la inversión: "))

# Calcular el capital obtenido cada año de la inversión
capital = inversion
for i in range(num_anios):
    capital = capital * (1 + interes_anual / 100)
    print("Capital después del año", i+1, ":", round(capital, 2))