#Escribir un programa que pida al usuario un número entero y muestre por pantalla si
#es un número primo o no.
num = int(input("Indica un numero: "))

contador = 0
for i in range (1, num+1):
    if (num % i == 0):
        contador = contador + 1

if contador <= 2:
    print ("El numero es PRIMO")
else:
    print ("El numero NO es PRIMO")
