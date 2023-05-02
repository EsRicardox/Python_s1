bencina = True
Encendido = True
Edad = 19


#########################################
#                                       #
#              El NOT                   #
#   invierte los comparadores de        #
#    NOT cambia de True a False         #
#    NOT cambia de False a True         #
#                                       #
#########################################

## Utilizar el operador AND

if bencina and Encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

## Utilizar el operador OR

if bencina or Encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

## Utilizar el operador NOT junto al AND

if not bencina and Encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

## Utilizar el operador NOT junto al OR

if not bencina or Encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

## Utilizar el operador NOT junto al OR y el AND >= "Edad"

if not bencina or (Encendido and Edad >=18):
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")
