#Condiciones

'''
En una determinada empresa, sus empleados son evaluados al final de cada año. Los
puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados
pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras
mencionadas. A continuación se muestra una tabla con los niveles correspondientes a
cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€
multiplicada por la puntuación del nivel.
'''
puntuacion = float(input("Introduce la puntuación del empleado: "))

if puntuacion == 0.0:
    nivel = "Insuficiente"
elif puntuacion == 0.4:
    nivel = "Aceptable"
elif puntuacion == 0.6:
    nivel = "Meritorio"
else:
    nivel = "Sobresaliente"

dinero_conseguido = 2400 * puntuacion

print("La puntuación del empleado es", puntuacion, "y su nivel es", nivel)
print("El dinero conseguido es", dinero_conseguido, "euros.")