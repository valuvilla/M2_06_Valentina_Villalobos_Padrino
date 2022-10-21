

def lee_numero():
    numero1=int(input("Dígito1: "))    
    numero2=int(input("Dígito2: "))  
    numero3=int(input("Dígito3: "))
    lista=list((numero1, numero2, numero3))
    print("La lista de valores es {}".format(lista))
    return numero1, numero2, numero3


def mayor():
    numero1, numero2, numero3 = lee_numero()
    mayor=max(numero1, numero2, numero3)
    print("Mayor número: {}".format(mayor))

    
mayor()





    
    



