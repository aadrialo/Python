#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#calcule el índice de masa corporal y lo almacene en una variable, y muestre por
#pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el
#índice de masa corporal calculado redondeado con dos decimales.

var1= float(input("Jefe cuanto pesas?"))
var2= float(input("Jefe cuanto mides?"))
imc= (var1 / (var2)**2)
imcRound= round(imc, 2)
print("Tu indice de masa corporal es ", imc ," donde ", imcRound ," es el indie de masa corporal calculado redondeando los dos decimales")