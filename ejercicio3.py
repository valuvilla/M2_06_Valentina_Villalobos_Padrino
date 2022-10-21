import sys
#Definimos la funcion que determinara el estado nutricional de la persona
def imc():
    #Pedimos por teclado la talla y peso
    altura=float(input("talla: "))
    peso_total=float(input("peso: "))

    #Acortamos los decimales del precio
    peso=float("{:.02f}".format(peso_total))

    #Realizamos la operacion
    IMC=(peso/(altura**2))

    #Comparamos resultados
    if IMC< 18.5:
        return "Su IMC es {}: Bajo de peso con un peso de {}kg y una talla de {}m".format(IMC,peso, altura)
    elif 18.5<IMC<25:
        return "Su IMC es {}: Normal con un peso de {}kg y una talla de {}m".format(IMC, peso, altura)
    elif 25<=IMC<30:
        return "Su IMC es {}: Sobrepeso con un peso de {}kg y una talla de {}m".format(IMC, peso, altura)
    else:
        return "Su IMC es {}: Obesidad con un peso de {}kg y una talla de {}m".format(IMC,peso, altura)

print(imc())