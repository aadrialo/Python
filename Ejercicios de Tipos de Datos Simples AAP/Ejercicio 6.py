#Escribir un programa que lea un entero positivo, , introducido por el usuario y
#después muestre en pantalla la suma de todos los enteros desde 1 hasta . La suma
#de los primeros enteros positivos puede ser calculada de la siguiente forma:
while True:
    numUser = int(input("Indica un numero: "))

    if numUser > 0:
        suma = numUser*((numUser+1)/2)
        print("La suma de los enteros desde 1 hasta", numUser, "es:", suma)
        break
    else:
        print("Recuerda que el número debe ser entero y positivo")
