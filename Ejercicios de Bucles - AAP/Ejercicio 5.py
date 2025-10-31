#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
#año que dura la inversión.
cantidad = float(input("Cuanto quieres invertir"))
interes = float(input("De cuanto es el interes"))
anios = int(input("Cuantos años"))
for i in range( 1 , anios+1 ):
    cantidad = cantidad * interes
    print ("En", i , "años, obtienes", cantidad ,"€")