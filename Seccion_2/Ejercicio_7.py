#Condiciones

'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación:

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
función de su respuesta le muestre un menú con los ingredientes disponibles para que
elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que
están en todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
vegetariana o no y todos los ingredientes que lleva.
'''

# Pedimos al usuario que introduzca si quiere una pizza vegetariana o no
es_vegetariana = input("¿Quieres una pizza vegetariana? (s/n): ")

# Si la respuesta es sí, mostramos los ingredientes vegetarianos disponibles
if es_vegetariana.lower() == "s":
    print("Estos son los ingredientes vegetarianos disponibles:")
    print("- Pimiento")
    print("- Tofu")
# Si la respuesta es no, mostramos los ingredientes no vegetarianos disponibles
else:
    print("Estos son los ingredientes no vegetarianos disponibles:")
    print("- Peperoni")
    print("- Jamón")
    print("- Salmón")

# Pedimos al usuario que elija un ingrediente y lo guardamos en una variable
ingrediente = input("Elige un ingrediente (además de la mozzarella y el tomate): ")

# Mostramos por pantalla si la pizza elegida es vegetariana o no, y todos los ingredientes que lleva
if es_vegetariana.lower() == "s":
    print("La pizza elegida es vegetariana y lleva mozzarella, tomate y", ingrediente)
else:
    print("La pizza elegida no es vegetariana y lleva mozzarella, tomate y", ingrediente)