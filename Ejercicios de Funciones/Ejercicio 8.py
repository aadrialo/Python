#Escribir una función que reciba una muestra de números en una lista y devuelva un
#diccionario con su media, varianza y desviación típica.
def cuadrado(muestra):
    lista_cuadrados = []
    for i in muestra:
        lista_cuadrados.append(i**2)
    return lista_cuadrados

def estadisticas(muestra):
    est = {}
    est['media'] = sum(muestra)/len(muestra)
    est['varianza'] = sum(cuadrado(muestra))/len(muestra)-est['media']**2
    est['desviacion tipica'] = est['varianza']**0.5
    return est

print (estadisticas([1, 2, 3, 4, 5]))
