estatura = 1.71
peso = 70
complejo = 1 + 4j
edad = 18

print("\n","\n","\n")
print(f"Mi estatura es de {estatura} y mi pero es de {peso}")
print("impresion de un numero complejo: ",complejo)

print("transformar un valor real a entero: ",int(peso))
print("transformar un valor entero a real: ",int(edad))

imc = peso / (estatura**2)

print("Mi IMC es de: ",imc,"\n")

print("Mi IMC es de: {:.2f}".format(imc),"\n")

print("\n","\n","\n")

##funciones propias de python

#string() -
#int()    -numeros enteros
#float()  -numeros decimales
#len()    -lee la cantidad de items en un lista
#type()   -
#count() -busca la cantidad de palabras iguales en una lista
#conunt() -buscador de info en codigo
#range("numero") - la lista la carga desde el 0 hasta el numero asignado
#range("num1,num2") la lista inicia en el num1 y termina en el num2
###
# data_asig = [10023,"programacion",1,True]
# cod,ramo,semestre,estado = data_asig
###

##fin de la lista


nueva_lista = list()
otra_lista = []
print ("Esta es una lista vacia :",nueva_lista)
print ("Esta es otra lista vacia :",otra_lista)

### diccionarios ###

diccionario1 = dict()
diccionario2 = {}
datos_personales = {
    "nombre":"ricardo",
    "Intitucion":"Ulagos",
    "Edad":18
}

print(datos_personales)

### dato agregado ###

datos_personales = {
    "nombre":"ricardo",
    "Intitucion":"Ulagos",
    "Edad":18,
    "Asisgnatira":{"Estructira de Datos","Programacion"}
}

print("Diccionario Inicial: ",datos_personales)

### llamando un dato con su clave ###

print(len(datos_personales))
print(datos_personales["Intitucion"])

### Actualizando listas ###

datos_personales["Asisgnatira"] = "USS"
print("Direccion actualizado 1 ",datos_personales)

datos_personales["Ciudad"] = "Osorno"
print("Direccion Actualizada 2 ",datos_personales)

### eliminar un dato del diccionario ###

del datos_personales["Ciudad"]
print("Direccion Actualizada 3 ",datos_personales)

