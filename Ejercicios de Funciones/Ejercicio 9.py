#Escribir una función que calcule el máximo común divisor de dos números y otra que
#calcule el mínimo común múltiplo.
def mcd(n, m):
    res = 0
    while(m > 0):
        res = m
        m = n % m
        n = res
    return n

def mcm(n, m):
    if n > m:
        mayor = n
    else:
        mayor = m
    while (mayor % n != 0) or (mayor % m != 0):
        mayor += 1
    return mayor

print(mcd(16,48))