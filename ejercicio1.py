import math

def area_circulo():
    radio=int(input(("introduce radio: ")))
    π=math.pi
    area=(radio**2)*π 
    return "El area del circulo de radio {} es {}".format(radio, area)  

print(area_circulo())