def is_multiple(n, mult):
    if n % mult == 1:
         return False

         return True

def numero_m(impar):
    while impar == 1:   
          if is_multiple(impar, 10):
           print(impar)
          num -= 1
          
num = (input("Entra un numero:  "))

numero_m(int(num))
