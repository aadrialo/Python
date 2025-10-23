#Escribir un programa que pida al usuario dos números y muestre por pantalla su
#división. Si el divisor es cero el programa debe mostrar un error.
num1 = int(input("Indica un numero: "))
num2 = int(input("Indica un numero: "))
if (num1 == 0 or num2 == 0):
    print("ERROR: Uno de los valores introducidos es 0")
