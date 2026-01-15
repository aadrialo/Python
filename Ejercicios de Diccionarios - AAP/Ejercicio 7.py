#Escribir un programa que cree un diccionario simulando una cesta de la compra. El
#programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta
#que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la
#compra y el coste total, con el siguiente formato
diccionario = {}
totalPrecio = 0
Pregunta1 = input("Quieres empezar a comprar? (si/no): ")
Pregunta1LOW = Pregunta1.lower()

if (Pregunta1LOW == "si"):
    while True:
        datoTEMP = input("¿Que articulo vas a comprar?: ")
        valorTEMP = float(input("¿Cual cuanto cuesta?: "))
        totalPrecio = totalPrecio + valorTEMP
        diccionario[datoTEMP] = valorTEMP
        continuar = input("¿Quieres añadir otro?(si/no): ")
        continuarLOW = continuar.lower()


        if continuarLOW == "no":
            print("LISTA DE LA COMPRA")
            print("_________________________________________")
            for producto, precio in diccionario.items():  
                print(f"El/La {producto} vale {precio}€ ")

            print("_________________________________________")
            print(f"TOTAL: {totalPrecio}")
            break
else:
    print("OK, ADIOS")