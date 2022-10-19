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
        return "Bajo de peso con un peso de {}kg y una talla de {}m".format(peso, altura)
    elif 18.5<IMC<25:
        return "Normal con un peso de {}kg y una talla de {}m".format(peso, altura)
    elif 25<=IMC<30:
        return "Sobrepeso con un peso de {}kg y una talla de {}m".format(peso, altura)
    else:
        return "Obesidad con un peso de {}kg y una talla de {}m".format(peso, altura)

print(imc())