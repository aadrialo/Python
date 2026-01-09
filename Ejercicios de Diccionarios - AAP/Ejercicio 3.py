#Escribir un programa que guarde en un diccionario los precios de las frutas de la
#tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
#precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe
#mostrar un mensaje informando de ello.


Fruta = {'Platano':1.35,'Manzana':0.80, 'Pera':0.85, 'Naranja':0.70}
frutaPregunta = input("¿Que fruta quieres consultar?")
if frutaPregunta in Fruta:
    Kilos = float(input("Cuantos kilos quieres"))
    precio = Fruta[frutaPregunta]
    precioTotal = Kilos * precio
    print(f"Te va a costar {precioTotal}€")
else:
    print ("ERROR: Esa fruta no existe en el catalogo")