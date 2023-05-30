num = int(input("Ingrese un numero: "))

if num % 2 ==0:
    print(f"El numero {num} es par.")
else:
    print(f"El numero {num} es impar.")

num2 = True
for i in range(2, num):
    if num % i == 0:
        num2 = False
        break

if num2:
    print(f"El numero {num} es primo")
else:
    print(f"El numero {num} no es primo")

if num > 50:
    print(f"El numero {num} es Mayor que 50")
elif num < 50:
    print(f"El numero {num} es Menor que 50")
else:
    print(f"El numero es igual ya que es 50")