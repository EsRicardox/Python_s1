a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]
abc=a+b+c
print(abc)
#--------------------------------
c = [2,3,8,9,20,12]
abc2 = a+b+c

print(abc2)
#--------------------------------
abc2 = sorted(abc2)
print(abc2)
#--------------------------------
d = [4,5,6]
abc3 = abc2+d
#--------------------------------
suma = sum(abc3)
print(suma)
#--------------------------------
abc4 = len(abc2)
print (suma/abc4)