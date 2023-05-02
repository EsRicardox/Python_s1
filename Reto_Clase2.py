diccionario = {
}

Nombre = input("Nombre: ")
Asignatura = input("La Asignatura: ")
Primera_nota = float(input("La Primera Nota del Laboratorio:: "))
Segunda_nota = float(input("La Segunda Nota del Laboratorio: "))

nf_1 = Primera_nota*0.3
nf_2 = Segunda_nota*0.7
nota_final = nf_1+nf_2

diccionario["Nombre"] = Nombre
diccionario["Asignatura"] = Asignatura
diccionario["Primera_Nota"] = Primera_nota
diccionario["Segunda_Nota"] = Segunda_nota
diccionario["nota_final"] = nota_final
print("el diccionario: ",diccionario)
