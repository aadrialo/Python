#Escribir un programa que pida al usuario un número entero y muestre por pantalla
#un triángulo rectángulo como el de más abajo, de altura el número introducido.
num=int(input("De cuantas filas debe ser"))
sim= "*"

for i in range(1,num+1,1):
    print (sim*i)
        