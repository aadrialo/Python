#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
#y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
#<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>

nombre = str(input("Cual es tu nombre: "))
edad = int(input("Cual es tu edad: "))
direccion = str(input("Donde vives: "))
telefono = int(input("Numero de telefono: "))

user = {'name':nombre , 'age':edad, 'direction':direccion, 'tlf':telefono}

print (f"{user['name']} tiene {user['age']} años, vive en {user['direction']} y su número de teléfono es {user['tlf']}")