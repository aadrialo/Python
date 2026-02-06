#Escribir una función que convierta un número decimal en binario y otra que convierta
#un número binario en decimal.
def a_decimal(n):
    digitos = list(n)
    digitos.reverse()
    decimal = 0
    for i in range(len(digitos)):
        decimal = decimal + int(digitos[i]) * 2 ** i
    return decimal

def a_binario(n):
    binario = []
    while n > 0:
        binario.append(str(n % 2))
        n = n // 2
    binario.reverse()
    return ''.join(binario)


print(a_binario(130))
print(a_decimal('10000010'))