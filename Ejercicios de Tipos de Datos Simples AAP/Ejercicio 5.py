#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
#coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
numHoras = int(input("¿Cuantas horas trabajaste?"))
pph = float(input("¿Cuanto cobras por hora?"))
sueldo = (numHoras*pph)
sueldoStr = str(sueldo)
print("Por las horas trabajadas cobraste en total: "+ sueldoStr+ "€")


