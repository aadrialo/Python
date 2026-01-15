#Escribir un programa que cree un diccionario de traducción español-inglés. El
#usuario introducirá las palabras en español e inglés separadas por dos puntos, y
#cada par <palabra>:<traducción> separados por comas. El programa debe
#crear un diccionario con las palabras y sus traducciones. Después pedirá una frase
#en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra
#no está en el diccionario debe dejarla sin traducir.
traductor = {}


while True:
    TempWord = input("Indica palabras en español:ingles (Separalas por 2 puntos): ")
    tempA = TempWord.split(":")[0]
    tempB = TempWord.split(":")[1]
    traductor[tempA] = tempB

    continuar = input("¿Quieres continuar? ").lower()
    if continuar == "no":
        break


while True:
    Frase = input("Di una frase: ")
    FraseSPLIT = Frase.split()

    for i in range(len(FraseSPLIT)):
        palabraActual = FraseSPLIT[i]
        if palabraActual in traductor:
            FraseSPLIT[i] = traductor[palabraActual]

    resultado = " ".join(FraseSPLIT)
    print(resultado)
    
    cont = input("\n¿Quieres seguir? (si/no): ").lower()
    if cont == "no":
        break