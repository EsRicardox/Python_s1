nombre=(input("cual es tu nombre?"))
edad= int(input("Cual es tu edad?"))
total_años = edad+20
print("Hola mi nombre es ",nombre,"tengo ",edad," años y en 20 años tendre ",total_años," años")


conjunto_colores= set({"azul","rojo","verde"})
conjunto_animalle= {"Gato","Perro","Loro"}
print(type(conjunto_colores))
print(type(conjunto_animalle))
print("El primer set contiene los siguientes colores: ",conjunto_colores)
print("El segundo set contiene los siguientes animales: ",conjunto_animalle)

conjunto_colores.add("Celeste")
print("El set de colores lo conforman: ",conjunto_colores )