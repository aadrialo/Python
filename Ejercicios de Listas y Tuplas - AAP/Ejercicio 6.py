#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
#nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
#aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
#usuario tiene que repetir.

asignaturas=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
asignatuasSuspensas=[]
aslen = len(asignaturas)

for i in range(aslen-1,-1,-1):
    print (asignaturas[i])
    NotaAsig=float(input("¿Que has sacado?"))

    if NotaAsig < 5:
        asignatuasSuspensas.append(asignaturas[i])
        asignaturas.pop(i)

print (f"Las asignaturas aprobadas son: {asignaturas}")
print (f"Las asignatuas suspensas son: {asignatuasSuspensas}")