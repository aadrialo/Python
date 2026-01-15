#Escribir un programa que cree un diccionario vacío y lo vaya llenado con
#información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo
#electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato
#debe imprimirse el contenido del diccionario.

diccionario = {}

Pregunta1 = input("Quieres empezar a darme tus datos? (si/no): ")
Pregunta1LOW = Pregunta1.lower()
if (Pregunta1LOW == "si"):
    while True:
        datoTEMP = input("¿Que dato me quieres dar?: ")
        valorTEMP = input("¿Cual es el valor del dato?: ")
        diccionario[datoTEMP] = valorTEMP
        print (diccionario.items())
        continuar = input("¿Quieres continuar?(si/no): ")
        continuarLOW = continuar.lower()
        if continuarLOW == "no":
            print (diccionario.items())
            break
else:
    print("OK, ADIOS")
