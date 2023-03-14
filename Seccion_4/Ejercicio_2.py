#Funciones

'''
Escribir una función que convierta un número decimal en binario y otra que convierta un
número binario en decimal. (Sin usar librerías)
'''

def decimal_a_binario(decimal):
    """
    Convierte un número decimal en binario.

    Args:
        decimal (int): Número decimal a convertir.

    Returns:
        str: Número en binario.
    """
    binario = ''
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    return binario

def binario_a_decimal(binario):
    """
    Convierte un número binario en decimal.

    Args:
        binario (str): Número binario a convertir.

    Returns:
        int: Número en decimal.
    """
    decimal = 0
    potencia = len(binario) - 1
    for d in binario:
        decimal += int(d) * 2 ** potencia
        potencia -= 1
    return decimal


binario = decimal_a_binario(14)
print(binario)
# Salida: '10011'


decimal = binario_a_decimal('1101')
print(decimal)
# Salida: 13