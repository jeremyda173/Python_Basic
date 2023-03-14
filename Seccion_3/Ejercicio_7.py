#Ciclos

'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que
repetir.
'''

asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
notas = []
for asignatura in asignaturas:
    nota = float(input(f"Introduce la nota de {asignatura}: "))
    notas.append(nota)
    
aprobadas = []
for i in range(len(asignaturas)):
    if notas[i] >= 5:
        aprobadas.append(asignaturas[i])
        asignaturas[i] = None

repetir = list(filter(lambda x: x is not None, asignaturas))

print("Asignaturas aprobadas:")
for asignatura in aprobadas:
    print(asignatura)

print("Asignaturas a repetir:")
for asignatura in repetir:
    print(asignatura)