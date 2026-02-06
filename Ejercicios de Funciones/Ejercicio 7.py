#Escribir una función que reciba una muestra de números en una lista y devuelva otra
#lista con sus cuadrados.
def cuadrado(sample):
    list = []
    for i in sample:
        list.append(i**2)
    return list
print(cuadrado([1, 2, 3, 4, 5]))
print(cuadrado([4.7, 5.2, 8.2, 11.1, 15.5]))