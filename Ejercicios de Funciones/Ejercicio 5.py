#Escribir una función que calcule el área de un círculo y otra que calcule el volumen
#de un cilindro usando la primera función.

def circarea(radio):
    pi = 3.1415
    return pi*radio**2

def cilindvolumen(radio, altura):
    return circarea(radio)*altura

print(cilindvolumen(7,9))