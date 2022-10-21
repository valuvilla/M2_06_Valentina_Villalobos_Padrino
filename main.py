

def lee_numero():
    valores=[]
    numero1=int(input("Dígito: "))    
    numero2=int(input("Dígito: "))  
    numero3=int(input("Dígito: "))
    valores.append(numero1, numero2, numero3)  
    print(valores)
    return numero1, numero2, numero3



def mayor():
    numero1, numero2, numero3 = lee_numero()
    mayor=max(numero1,numero2, numero3)
    return "El mayor numero es el {}".format(mayor)


mayor()




    
    



