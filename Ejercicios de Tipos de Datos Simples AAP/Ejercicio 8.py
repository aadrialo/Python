#Escribir un programa que pida al usuario dos números enteros y muestre por
#pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde
#<n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente
#y el resto de la división entera respectivamente.
var1 = int(input("Dame un numero entero")) 
var2 = int(input("Dame otro numero entero")) 
cociente = var1 / var2
resto = var1 % var2

print(var1 ,"entre", var2 ,"da un cociente", cociente ,"y un resto", resto ,"donde", var1 ," y ", var2 ,"son los números introducidos por el usuario, y", cociente ,"y", resto ,"son el cociente y el resto de la división entera respectivamente.")