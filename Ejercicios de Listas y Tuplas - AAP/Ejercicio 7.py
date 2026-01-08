#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
#letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista
#resultante.

abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
letrasEl = []
abcLen = len(abecedario)
while abcLen % 3 != 0:
    abcLen = abcLen +1 

for i in range(abcLen,-1,-3):
    abecedario.pop(i)

print(abecedario)