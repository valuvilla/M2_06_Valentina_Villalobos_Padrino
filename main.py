

def lee_numero():
    numero1=int(input("Introduce dígito1: "))    
    numero2=int(input("Introduce dígito2: "))  
    numero3=int(input("Introduce dígito3: "))
    lista=list((numero1, numero2, numero3))
    print("La lista de valores es {}".format(lista))
    return numero1, numero2, numero3


def mayor():
    numero1, numero2, numero3 = lee_numero()
    mayor=max(numero1, numero2, numero3)
    return "Mayor número: {}".format(mayor)

    
print(mayor())






    
    



