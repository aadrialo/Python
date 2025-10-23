#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
#dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
#anterior para que también funcione cuando el día o el mes se introduzcan con un
#solo carácter.
fechaNac = str(input("Indica tu fecha de nacimiento (dd/mm/aaaa)"))
fechaSplit = fechaNac.split("/")
print ("El dia de nacimiento es ", fechaSplit[0], " el mes es ", fechaSplit[1], "y el año es ", fechaSplit[2])