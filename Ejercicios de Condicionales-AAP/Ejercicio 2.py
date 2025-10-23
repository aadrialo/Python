#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña e imprima por pantalla si la
#contraseña introducida por el usuario coincide con la guardada en la variable sin
#tener en cuenta mayúsculas y minúsculas.
contrasenia = str(input("Ingrese su contraseña: "))
PassCheck = str (input("ingresa la contraseña otra vez: "))
contraseniaL = contrasenia.lower()
PassCheckL = PassCheck.lower()
while True:
    if (contraseniaL == PassCheckL):
        print("La contraseña es correcta")
        break
    else:
        print("Contraseña Incorrecta ")