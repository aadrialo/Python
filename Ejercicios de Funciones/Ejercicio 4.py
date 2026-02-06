#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La
#función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el
#total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá
#aplicar un 21%
def calcIVA(cant, iv=21):
    return cant + cant*iv/100

print(calcIVA(1200,10))
print(calcIVA(1200))