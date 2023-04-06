import math
import time
import os
 
def espacio(x):
    if x >= 1:
        print("")
        x = x-1
 
wait = time.sleep
blank = os.system('cls')
 
while True:
    print("""Selecciona la operacion deseada:
1.Suma
2.Resta
3.Multiplicacion
4.Division8
5.Division exacta
6.Potencia
7.Apagar calculadora""")
    espacio(1)
 
    c=int(input())
 
    if c == 7:
        print ("Gracias por usar esta calculadora")
        wait(2)
        quit()
 
    else:
        print("Escribe el primer numero")
        a=int(input())
        print("Escribe el segundo numero")
        b=int(input())
        espacio(2)
        print("El resultado de esta operacion és:")
 
        if c == 1:
            print(a+b)
            print("")
        if c == 2:
            print(a-b)
            print("")
        if c == 3:
            print(a*b)
            print("")
        if c == 4:
            print(a/b)
            print("")
        if c == 5:
            print(a//b)
            print("")