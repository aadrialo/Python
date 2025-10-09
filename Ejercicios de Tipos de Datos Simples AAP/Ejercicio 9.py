#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión.
inv= float(input("Cuanto quieres invertir?"))
intereses=float(input("Tasa de interes?"))
años=float(input("Cuantos años?"))

intTot= inv*(intereses/100)*años
print ("capital obtenido en la inversion: ", intTot)