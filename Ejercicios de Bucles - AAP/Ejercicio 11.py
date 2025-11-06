#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
#una a una las letras de la palabra introducida empezando por la última.
palabra = str(input("Di 1 palabra"))
for i in reversed(palabra):
    print (i)

