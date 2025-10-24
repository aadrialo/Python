#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla
#el tipo impositivo que le corresponde
renta = float(input("¿Cual es tu renta anual?"))
if renta < 0:
    impositivo = "Renta no válida (no puede ser negativa)"
elif renta < 10000:
    impositivo = "5%"
elif renta <= 20000:  
    impositivo = "15%"
elif renta <= 35000:  
    impositivo = "20%"
elif renta <= 60000:  
    impositivo = "30%"
else:  
    impositivo = "45%"

print("El impositivo es: ", impositivo)