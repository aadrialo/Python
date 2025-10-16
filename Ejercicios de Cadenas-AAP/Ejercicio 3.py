#Escribir un programa que pregunte el nombre del usuario en la consola y después
#de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n>
#letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el
#número de letras que tienen el nombre.
nameUser = str(input("¿Cual es tu nombre?"))
letrasCantidadUser = len(nameUser)
print (nameUser, " tiene ", letrasCantidadUser, " letras, donde ", nameUser.upper(), "es el nombre de usuario en mayusculas y ", letrasCantidadUser, "es el numero de letras que tiene el nombre" )
