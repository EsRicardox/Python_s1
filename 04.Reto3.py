Ciudades = ["Santiago", "Temuco","Osorno","Punta Arenas"]
inci_aire = [134,99,255,50]

max_aire = inci_aire.index(max(inci_aire))
min_aire = inci_aire.index(min(inci_aire))


print(f"La calidad del indice del aire mas bajo es {Ciudades[min_aire]} con un indice de {inci_aire[min_aire]}")
print(f"La calidad del indice del aire mas Alto es {Ciudades[max_aire]} con un indice de {inci_aire[max_aire]}")



for i in range(len(Ciudades)):
    if inci_aire[i] >= 0 and inci_aire[i] <= 50:
        print(Ciudades[i],"Tiene una calidad del aire Buena")
    elif inci_aire[i] >= 51 and inci_aire[i] <= 100:
        print(Ciudades[i],"Tiene una calidad del aire Moderada")
    elif inci_aire[i] >= 101 and inci_aire[i] <= 150:
        print(Ciudades[i],"Tiene una calidad del aire dañina para la Salud de un grupo sensible")
    elif inci_aire[i] >= 151 and inci_aire[i] <= 200:
        print(Ciudades[i],"Tiene una calidad del aire dañina para la Salud")
    elif inci_aire[i] >= 201 and inci_aire[i] <= 300:
        print(Ciudades[i],"Tiene una calidad del aire MUY DAÑINA para la Salud")
    else:
        print("Tiene una calidad del aire PELIGROSA salga del lugar ahora")