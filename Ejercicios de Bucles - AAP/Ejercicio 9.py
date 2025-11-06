#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
#correcta.
contrasenia = str(input("Introduce tu contraseña: "))
while True:
    ContraseniaCheck = str(input("Cual es tu contraseña?: "))
    if (ContraseniaCheck == contrasenia):
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")