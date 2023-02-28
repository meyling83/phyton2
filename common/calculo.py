def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b!=0:
        return a/b
    
def mensaje(operacion,resultado):
    print(f"la {operacion} es {resultado:.2f}")


def metros_cuadrados(largo,ancho):
    return largo*ancho