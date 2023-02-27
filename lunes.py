def calcular_cuenta(cuenta,propina=10):
    total=cuenta + cuenta*propina*0.01
    total=round(total,2)
    return total

def calcular_total(*args):
    total=0
    for numero in args:
        total+=numero
    print(total)

def imprimir_dias_semana(*args):
    contador=0
    for dia in args:
        contador+=1
        print(f"{dia} es el {contador} dia de la semana")

if __name__=="__main__":
    """ imprimir_dias_semana("lunes","martes","miercoles","jueves","viernes")
    print("-"*10)
    imprimir_dias_semana("lunes","martes","miercoles","jueves","viernes","sabado","domingo") """
    #calcular_total(5,4,3,2,1,10,20)
"""     total=calcular_cuenta(100)
    print(f"hay que pagar ${total}")

    total=calcular_cuenta(100,12)
    print(f"hay que pagar ${total}") """
 
    

    