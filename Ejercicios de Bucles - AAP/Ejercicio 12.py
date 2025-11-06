#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
#muestre por pantalla el número de veces que aparece la letra en la frase.
palabra = str(input("Di tu palabra: "))
letra = str(input("Di tu letra: "))
contador = 0

for i in range (0,len(palabra),1):
    if palabra[i] == letra:
        contador = contador + 1
    
print(f"La letra {letra} aparece {contador} veces en la frase.")

        