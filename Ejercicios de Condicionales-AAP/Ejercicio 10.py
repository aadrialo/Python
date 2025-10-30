#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#Los ingredientes para cada tipo de pizza aparecen a continuación.
#● Ingredientes vegetarianos: Pimiento y tofu.
#● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
#en función de su respuesta le muestre un menú con los ingredientes disponibles
#para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
#tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
#pizza elegida es vegetariana o no y todos los ingredientes que lleva.

pizza= str(input("Quiere pizza vegetariana? Indique Si o No: "))
optLow = pizza.lower()
if ( optLow == "si" ):
    print ("Puedes elegir los siguientes ingredientes \n -Pimiento \n -Tofu")
    tempProd= str(input("indique el ingrediente: "))
    tempSTR=tempProd.lower()
    if ( tempSTR == "pimiento" or tempSTR == "tofu" ):
        print ("La pizza lleva mozzarella, tomate y", tempProd)
    else:
        print ("Ingrediente no valido")

elif (optLow == "no" ):
    print ("Puedes elegir los siguientes ingredientes \n -Peperoni \n -Jamon \n -Salmon")
    tempProd= str(input("indique el ingrediente: "))
    tempSTR=tempProd.lower()
    if ( tempSTR == "peperoni" or tempSTR == "jamon" or tempProd == "salmon" ):
        print ("La pizza lleva mozzarella, tomate y", tempProd)
    else:
        print ("Ingrediente no valido")

 