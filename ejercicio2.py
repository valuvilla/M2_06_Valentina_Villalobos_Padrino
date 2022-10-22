#Definimos la funcion que nos permita leer un número
def lee_numero():
    #pedimos tres veces un numero por teclado
    numero1=int(input("Introduce dígito1: "))    
    numero2=int(input("Introduce dígito2: "))  
    numero3=int(input("Introduce dígito3: "))

    #creamos una lista que los agrupe para poder mostrarlos por pantalla
    lista=list((numero1, numero2, numero3))
    print("La lista de valores es {}".format(lista))

    #Pedimos que nos devuelva los valores que hemos establecido
    return numero1, numero2, numero3


def mayor():
    #Con los datos de la funcion lee_numero(), obtenemos los tres paramentros
    numero1, numero2, numero3 = lee_numero()

    #Determinamos el mayor de los tres
    mayor=max(numero1, numero2, numero3)

    #Mostramos el resultado por pantalla
    return "Mayor número: {}".format(mayor)

    
print(mayor())