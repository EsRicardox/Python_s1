Tem_min={9,5,2,7,6,1}
Tem_max={12,14,11,10,15,9}


###-1

if 9 in Tem_min and 9 in Tem_max:
    print("La tempera 9 esta en ambos sets")
else:
    print("La tempera 9 No esta en ambos sets")


###-2

if 6 in Tem_min and 6 in Tem_max or 17 in Tem_min and 17 in Tem_max:
    if 6 in Tem_min and 6 in Tem_max:
        print("Esta la temperatura 6 esta en ambos sets")
    if 17 in Tem_min and 17 in Tem_max:
        print("Esta la temperatura 6 esta en ambos sets")
else:
    print("No esta la temperatura 6 y 17 en ambos sets")

###-3
Tem_min4 = [x ** 4 for x in Tem_max]
Tem_max4 = [x ** 4 for x in Tem_min]

print(Tem_max4)
print(Tem_min4)

###-4
sets = [Tem_min4, Tem_max4]
print(sets)
