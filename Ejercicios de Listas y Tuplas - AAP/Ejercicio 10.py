#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla 
#el menor y el mayor de los precios.

precio = [50, 75, 46, 22, 80, 65, 8]
menor = 99999999999999
mayor = -99999999999999

for i in range(0,len(precio)):
    if mayor < precio[i]:
        mayor = precio[i]
    if menor > precio[i]:
        menor = precio[i]

print(f"Mayor: {mayor}\nMenor: {menor}")
