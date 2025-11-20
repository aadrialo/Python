#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por
#pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada
#una de las asignaturas de la lista.

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
cantidad = len(asignaturas)
for i in range (0,cantidad):
    print ("Yo estudio",asignaturas[i])
