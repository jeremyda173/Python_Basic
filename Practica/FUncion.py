#Funcion

#Declaracion de la funcion
def horno(panes):
    print("Hornear una cantidad de panes...")
    print(panes)
    
#Usar la funcion
horno(3)
horno(5)


#Ejemplo 2

PASSWORD = "NINILINDO"

#Declaracion de a funcion
def login(pass_user):
    intentos = 3
    while PASSWORD != pass_user and intentos > 0:
       pass_user = input("Incorrecto, escribe tu password nuevamente!! ")
       intentos = intentos - 1
       
       
       if PASSWORD == pass_user:
           print("Estas logeado!!")
       elif intentos == 0:
           print("Tus intentos se agotaron, usuario bloqueado!!")




#Usar la funcion
password = input("Ingresa tu  password ")
login(password)

