#Escribir una función que reciba un número entero positivo y devuelva su factorial
def factorial(n):
    temp = 1
    for i in range(n):
        temp *= i+1
    return temp

print(factorial(4))
print(factorial(20))