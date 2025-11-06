#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range (1,11,1):
    print ("\nTabla del", i)
    for n in range (1,11,1):
        print(i,"x",n,"=",i*n)