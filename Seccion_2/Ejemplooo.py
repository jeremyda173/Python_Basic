#Factorial de un numero
#fact(0) = 1
#fact(0) = 1


def factorial_recursivo(n):
    
    #Caso base
    if n == 1 or n == 0:
        return 1
    
    #Caso revursivo
    return n * factorial_recursivo(n-1)

resultado = factorial_recursivo(6)
print(resultado)


#Factorial de un numero peroen ciclos

def factorial_ciclo(n):
    
    #Caso base
    if n == 1 or n == 0:
        return 1
    
    while n:
        
        if n == 1:
            return n
        
    return n * factorial_recursivo(n-1)

resultado = factorial_ciclo(2)
print(resultado)
