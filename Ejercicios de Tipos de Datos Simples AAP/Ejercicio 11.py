#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
#interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
#año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que
#comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
#introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
#la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada
#cantidad a dos decimales.

ingresar = float(input("¿Cuanto quieres depositar?"))
earnings = (ingresar*0.04)
TotalEarnings= (ingresar + earnings)
print("Las ganancias el primer año serian", round(TotalEarnings,2))
print("Las ganancias el segundo año serian", round(TotalEarnings*2,2))
print("Las ganancias el tercer año serian", round(TotalEarnings*3,2))
