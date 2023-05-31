#Utilizando ciclos se pide construya un programa que permita 
#imprimir en la salida estándar
#la siguiente pirámide 
a = 10

for i in range(1, a + 1):
    
    numero = 1  
 
    for j in range(0, i):      
        print(numero, end="") 
        numero += 1  
        
    print()