#Escribir un programa que pregunte por consola el precio de un producto en euros
#con dos decimales y muestre por pantalla el número de euros y el número de
#céntimos del precio introducido.
priceProduct = float(input("¿Cual es el precio?"))
priceProduct = round(priceProduct, 2)
priceProduct = str(priceProduct)
Precios = priceProduct.split(".")
print("El numero de euros son "+ Precios[0] +" y el numero de centimos son ", Precios[1])

