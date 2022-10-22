import sys
#Definimos la funcion que determinara el estado nutricional de la persona
def imc():
    #Pedimos por teclado la talla y peso
    altura=float(input("talla en metros: "))
    peso_total=float(input("peso en kg: "))

    #Acortamos los decimales del precio
    peso=float("{:.02f}".format(peso_total))

    #Realizamos la operacion
    IMC=(peso/(altura**2))

    #Comparamos resultados
    if IMC< 18.5:
        return "IMC: {}.Esto implica bajo de peso con un peso de {}kg y una talla de {}m".format(IMC,peso, altura)
    elif 18.5<IMC<25:
        return "IMC: {}. Esto implica normal con un peso de {}kg y una talla de {}m".format(IMC, peso, altura)
    elif 25<=IMC<30:
        return "IMC: {}. Esto implica sobrepeso con un peso de {}kg y una talla de {}m".format(IMC, peso, altura)
    else:
        return "IMC: {}. Esto implica obesidad con un peso de {}kg y una talla de {}m".format(IMC,peso, altura)

print(imc())