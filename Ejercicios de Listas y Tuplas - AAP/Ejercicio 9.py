#Escribir un programa que pida al usuario una palabra y
#muestre por pantalla el número de veces que contiene cada 
#vocal.

palabra = input("Di una palabra: ").lower()
vocales = ['a','e','i','o','u']
counterA = 0
counterE = 0
counterI = 0
counterO = 0
counterU = 0

palabra = list(palabra)
for i in range(0,len(palabra)):
    for z in range(0,len(vocales)):
        if palabra[i] == vocales[z]:
            if vocales[z] == "a":
                counterA = counterA + 1
            elif vocales[z] == "e":
                counterE = counterE + 1
            elif vocales[z] == "i":
                counterI = counterI + 1
            elif vocales[z] == "o":
                counterO = counterO + 1
            elif vocales[z] == "u":
                counterU = counterU + 1

print(f"A:{counterA}\nE:{counterE}\nI:{counterI}\nO:{counterO}\nU:{counterU}\n")