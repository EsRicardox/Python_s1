
a = input("Ingresa una palabra: ").lower()

b = a[::-1]  

if a == b:
    print(f"'{a}' es un palíndromo")  
else:     
    print(f"'{a}' no es un palíndromo")