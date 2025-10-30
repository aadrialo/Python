#En una determinada empresa, sus empleados son evaluados al final de cada año.
#Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
#aumentando, traduciéndose en mejores beneficios. Los puntos que pueden
#conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores
#intermedios entre las cifras mencionadas. A continuación se muestra una tabla con
#los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida
#en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
puntos= float(input("Cuantos puntos tienes?"))
if (puntos == 0.0):
    puntosSTR= str(puntos)
    print ("La cantidad de dinero que nadas, seria de ", puntosSTR )
elif (puntos == 0.4):
    temp= 2400*puntos
    strTemp= str(temp)
    print ("La cantidad de dinero que nadas, seria de ", strTemp )
elif (puntos >= 0.6):
    temp= 2400*puntos
    strTemp= str(temp)
    print ("La cantidad de dinero que nadas, seria de ", strTemp )
else :
    print ("Valor invalido")
