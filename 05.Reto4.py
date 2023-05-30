
nom1 = str(input("Ingrese el nombre del primer pacientes que quieras registrar :"))
nom2 = str(input("Ingrese el nombre del segundo pacientes que quieras registrar :"))
nom3 = str(input("Ingrese el nombre del trecero pacientes que quieras registrar :"))
print("------")
pes1 = float(input("Ingrese el peso de los tres pacientes :"))
pes2 = float(input("Ingrese el peso de los tres pacientes :"))
pes3 = float(input("Ingrese el peso de los tres pacientes :"))
print("------")
if pes1 >= 0 and pes2 >= 0 and pes3 >= 0:
    est1= float(input("Ingrese la estatura de los tres pacientes :"))
    est2= float(input("Ingrese la estatura de los tres pacientes :"))
    est3= float(input("Ingrese la estatura de los tres pacientes :"))
    print("------")
    if est1 >= 0.10 and est2 >= 0.10 and est3 >= 0.10:

        
        eda1 = int(input("Ingrese la edad de los tres pacientes :"))
        eda2 = int(input("Ingrese la edad de los tres pacientes :"))
        eda3 = int(input("Ingrese la edad de los tres pacientes :"))
        print("------")
        if eda1 >= 0 and eda2 >= 0 and eda3 >= 0 and eda1 <= 120 and eda2 <= 120 and eda3 <= 120:
            print("---Todo---")
            tupla = [(nom1,est1,pes1,eda1),(nom2,est2,pes2,eda2),(nom3,est3,pes3,eda3)]
            print(" : ",tupla)
        else:
            print("Error al digitar intentelo mas tarde")
    else:
        print("Error al digitar intentelo mas tarde")
else:
    print("Error al digitar intentelo mas tarde")






