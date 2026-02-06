#Escribir una función que reciba una muestra de números en una lista y devuelva su
#media.
def media(sample):
    """Función que calcula la media de una muestra de números.
    Parámetros
    sample: Es una lista de números
    Devuelve la media de los números en sample. 
    """
    return sum(sample)/len(sample)

print(media([1, 2, 3, 4, 5]))
print(media([4.7, 5.2, 8.2, 11.1, 15.5]))