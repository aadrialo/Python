#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
#un descuento del 60%. Escribir un programa que comience leyendo el número de
#barras vendidas que no son del día. Después el programa debe mostrar el precio
#habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
#coste final total.

noDay = int(input("¿Cuantas barras que no son del dia vendiste?"))
normalPrice = float(3.49)
PanPricenoDay = (normalPrice-(3.49*0.6))
TotalPrice= round((PanPricenoDay*noDay),2)
PriceRound= (round(PanPricenoDay,2))
print("El precio normal del pan es de ", normalPrice, "€, pero al no ser del dia se hace un 60% de descuento por lo que el precio de la barra de pan seria", PriceRound, "€ y el precio total de las ganancias de esto panes ha sido de: ", TotalPrice,"€" )