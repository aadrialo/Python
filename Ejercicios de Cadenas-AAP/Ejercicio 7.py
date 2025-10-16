#Escribir un programa que pregunte el correo electrónico del usuario en la consola y
#muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante
#de la arroba @) pero con dominio ceu.es.
nameEmail = str(input("Pon el nombre del correo: "))
EmailArroba = nameEmail.split("@")[0]
EmailCompleto = EmailArroba + "@ceu.es"
print ("el correo es: "+ EmailCompleto)