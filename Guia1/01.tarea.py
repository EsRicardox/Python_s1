#Realizar un algoritmo que indique el n´umero menor y el n´umero mayor entre tres
#enteros leidos por consola. Solo se deben ingresar n´umeros enteros.

a = int(input("Dime un numero: "))
b = int(input("Dime otro numero: "))
c = int(input("Dime otro numero: "))

abc = [a,b,c]
max = abc.index(max(abc))
min = abc.index(min(abc))
print("--Resultado--")
print("el numero mayor es: ",abc[max])
print("el numero menor es: ",abc[min])
