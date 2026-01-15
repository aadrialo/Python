#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre
#por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es
#el nombre del mes

meses ={
    "01":"enero",
    "02":"febrero",
    "03":"marzo",
    "04":"abril",
    "05":"mayo",
    "06":"junio",
    "07":"julio",
    "08":"agosto",
    "09":"septiembre",
    "10":"octubre",
    "11":"noviembre",
    "12":"diciembre"
}

pregunta = input("Indica la fecha en dd/mm/aaaa: ")
preguntaSplit = pregunta.split("/")[1]

if preguntaSplit in meses:
    dia = pregunta.split("/")[0]
    diaInt = int(dia)
    if  (diaInt > 31 and diaInt <= 0):
        mes = meses[preguntaSplit]
        año = pregunta.split("/")[2]
        print (f"La fecha sería: {dia} de {mes} del año {año}")
    else:
        print("Dia inexistente")
else:
    print("NO EXISTE ESE MES")
