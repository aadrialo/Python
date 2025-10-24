#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
#el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
#los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
#programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
#que le corresponde.


nombre = input("Introduce tu nombre: ")
nombre = nombre.upper() 
sexo = input("Introduce tu sexo (M para mujer, H para hombre): ")
sexo = sexo.upper()

inicial = nombre[0]
grupo = "B"

if sexo == "M":
    if inicial < "M":
        grupo = "A"
elif sexo == "H":
    if inicial > "N":
        grupo = "A"

print("Tu grupo es el", grupo)