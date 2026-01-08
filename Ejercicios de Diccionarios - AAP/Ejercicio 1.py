#Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
#'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su
#símbolo o un mensaje de aviso si la divisa no está en el diccionario

Coin = {'Euro':'€','Dollar':'$', 'Yen':'¥'}
divisaRequerida = input("¿Que divisa quiere usar?")
if divisaRequerida in Coin:
    print(Coin[divisaRequerida])
else:
    print ("ERROR: DIVISA INVALIDA")