import requests

def imprimirMensaje(lenguaje):
    print(f"{lenguaje} es un lenguaje de programacion.")

def calculo(a):
    return a+a+a

#calcula la suma de dos numeros
def sumar(numero1,numero2):
    return numero1+numero2

#calcula la diferencia entre dos numeros
def restar(numero1,numero2):
    return numero1-numero2


def pagina():
    link="http://info.cern.ch"
    r=requests.get(link)
    print(r.status_code)
    html=r.text.replace("the first website","my website")
    print(html) 


def validar_usuario(nombre,apellido,usuario,contraseña):
    lista=["password","contraseña","123456"]
    if len(usuario)<=5:
        return "El nombre de usuario tiene que ser mayor que 5"
    elif len(contraseña)<=6:
        return "La contraseña tiene que ser mayor que 6"
    elif contraseña in lista:
        return "La contraseña no es correcta"
    else: 
        return "Bienvenido " + str(nombre).swapcase() + " " + str(apellido).swapcase()
    
    


#este codigo tengo que ponerlo para ejecutar este archivo como mi programa principal. si importo este archivo, en donde lo importe este codigo no se ejecuta   
if __name__=='__main__':
    #imprimirMensaje("Python")
    #y=calculo(5)
   #print(y)
    """ numero1=float(input("Entre un sumando"))
    numero2=float(input("Entre otro sumando"))
    suma=sumar(numero1,numero2)
    print(f"la suma es {suma}") """

    """ numero1=float(input("Entre el minuendo"))
    numero2=float(input("Entre el sustraendo"))
    diferencia=restar(numero1,numero2)
    print(f"la diferencia es {diferencia}") """

    #pagina()  