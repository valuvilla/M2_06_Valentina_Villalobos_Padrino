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
        return "bajo de peso"
    elif 18.5<IMC<25:
        return "Normal"
    elif 25<=IMC<30:
        return "Sobrepeso"
    else:
        return "Obesidad"

print(imc())