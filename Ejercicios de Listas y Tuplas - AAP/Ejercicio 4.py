#Escribir un programa que pregunte al usuario los números ganadores de la lotería
#primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
#a mayor.

winnerNum=[]
cantidad=int(input("Cuantos numeros ganadores hay?: "))

for i in range(0,cantidad):
    temp = int(input(f"Indica el numero ganador {i+1}º: "))
    winnerNum.append(temp)

winnerNum.sort()
print("LOS NUMEROS GANADORES SON: ")
for i in winnerNum:
    print (i)