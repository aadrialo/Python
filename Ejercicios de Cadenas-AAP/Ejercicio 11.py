#Escribir un programa que pregunte el nombre el un producto, su precio y un número
#de unidades y muestre por pantalla una cadena con el nombre del producto seguido
#de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
#tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
nomProd = str(input("Nombre del producto"))
priceProd = float(input("Precio del producto"))
stkProd = int(input("Numero de unidades del producto"))

precio = priceProd * stkProd
print ("el producto es: ", nomProd," cuesta",f"{priceProd:09.2f}"," euros, el numero de unidades es ",f"{stkProd:03d}"," y el coste total es de ", f"{precio:011.2f}", "euros")