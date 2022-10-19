import math #importamos math para definir bien el numero pi
import sys
#Defimos la operacion del area
def area_circulo():
    #Pedimos el radio por pantalla
    radio=int(input(("introduce radio: ")))
    π=math.pi
    #Realizamos la operacion 
    area=(radio**2)*π 

    #pedimos que nos devuelva el resultado
    return "El area del circulo de radio {} es {}".format(radio, area)  

print(area_circulo())