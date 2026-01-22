#Escribir un programa que pida al usuario una palabra y muestre 
#por pantalla si es un palíndromo.
palabra = input("Di una palabra: ")
palabra = list(palabra)
if palabra == palabra[::-1]:
    print ("Es palindromo")
else:
    print ("No es palindromo")
