#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
#que el usuario escriba “salir” que terminará.
while True:
    eco = str(input(""))
    if eco == "salir":
        break
    else:
        print (eco) 