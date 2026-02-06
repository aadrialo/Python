#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario
#con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el
#diccionario generado con la función anterior y devuelva una tupla con la palabra más
#repetida y su frecuencia.
def cuentaPalabras(texto):
    lista_palabras = texto.split()
    frecuencias = {}
    for palabra in lista_palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def masRepetida(diccionario_palabras):
    palabra_max = ''
    frecuencia_max = 0
    for palabra, frecuencia in diccionario_palabras.items():
        if frecuencia > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frecuencia
    return palabra_max, frecuencia_max

frase = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(cuentaPalabras(frase))
print(masRepetida(cuentaPalabras(frase)))