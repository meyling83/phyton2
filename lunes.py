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

def ref_demo(x):
    x=42
    print(x)

def incrementar_ciudades(cities):
    cities.append("madrid")
    print(cities)

if __name__=="__main__":
    ciudades=["san sebastian","bilbao"]
    incrementar_ciudades(ciudades)
    print(ciudades)
    """     x=100
    ref_demo(x)
    print(x) """
    """ imprimir_dias_semana("lunes","martes","miercoles","jueves","viernes")
    print("-"*10)
    imprimir_dias_semana("lunes","martes","miercoles","jueves","viernes","sabado","domingo") """
    #calcular_total(5,4,3,2,1,10,20)
"""     total=calcular_cuenta(100)
    print(f"hay que pagar ${total}")

    total=calcular_cuenta(100,12)
    print(f"hay que pagar ${total}") """
 
    

    