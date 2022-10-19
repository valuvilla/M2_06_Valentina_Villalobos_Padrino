

def lee_numero():
    numero1=int(input("Dígito: "))    
    numero2=int(input("Dígito: "))  
    numero3=int(input("Dígito: "))     
    return numero1, numero2, numero3



def mayor(numero1, numero2, numero3):
    numero1, numero2, numero3 = lee_numero()
    if numero1 < numero2 < numero3:
        return "Mayor: {}".format(numero3)
    elif numero3 < numero1 < numero2:
        return "Mayor: {}".format(numero2)
    if numero2 < numero3 < numero1:
        return "Mayor: {}".format(numero1)

print(mayor(None, None, None))




    
    



