import funciones
import validar

""" def hola():
    usuario=input("Entre el nombre")
    print(f"Bienvenido {usuario}") """

#puedo pasar valor por defecto a los parametros de la funcion de esta forma. Tiene dos parametros a y b, que tienen por defecto hola los dos
""" def imprimir(a,b="Hello"):
    print(a,b) """

#con *args paso un grupo de parametros
""" def imprimirNumeros(*args):
    print(args) """
if __name__=='__main__':
    nombre=input("introduce el nombre")
    apellido=input("introduce el apellido")
    valido=False
    while valido==False:
        usuario=input("introduce tu usuario")
        valido=validar.validar_usuario(usuario)
    while valido==False:
        contraseña=input("introduce la contraseña")
        valido=validar.validar_contraseña(contraseña)
    print("Bienvenido " + nombre + " " + apellido) 

    
    #puedo llamar a la funcion sin pasar parametros, o pasando solo uno, los que no pase cogen por defecto el valor que tenian por defecto
    #imprimir("hola")
    #puedo pasar ambos parametros
    #imprimir("hola","kaixo")
    #puedo invertir el orden en el que paso los parametros
    #imprimir(b="hola",a="kaixo")

    #uso del *args, paso los parametros que quiera
    #imprimirNumeros("hola","mundo","ssss")
    #hola()

 
    
   








    """ numero1=float(input("Entre un sumando"))
    numero2=float(input("Entre otro sumando"))
    suma=funciones.sumar(numero1,numero2)
    print(f"la suma es {suma}") """

    """ numero1=float(input("entre el minuendo"))
    numero2=float(input("entre el sustraendo"))
    diferencia=funciones.restar(numero1,numero2)
    print(f"la diferencia es {diferencia}") """

""" funciones.pagina()  

nombre=input("Entre el nombre")
apellido=input("Entre el apellido")
nombre_usuario=input("Entre el nombre de usuario")
contraseña=input("Entre la contraseña")
texto=funciones.validar_usuario(nombre,apellido,nombre_usuario,contraseña)
print(texto) """

