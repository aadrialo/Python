#Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla la cuenta atrás desde ese número hasta cero separados por comas.
num = int(input("Indica un número: "))
if (num <= 0):
    print("Valor no valido")

else:
    for i in range(num, 0, -1):
        print(i, end=", ")