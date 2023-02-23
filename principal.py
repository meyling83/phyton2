import funciones

if __name__=='__main__':
    """ numero1=float(input("Entre un sumando"))
    numero2=float(input("Entre otro sumando"))
    suma=funciones.sumar(numero1,numero2)
    print(f"la suma es {suma}") """

    """ numero1=float(input("entre el minuendo"))
    numero2=float(input("entre el sustraendo"))
    diferencia=funciones.restar(numero1,numero2)
    print(f"la diferencia es {diferencia}") """

funciones.pagina()  

nombre=input("Entre el nombre")
apellido=input("Entre el apellido")
nombre_usuario=input("Entre el nombre de usuario")
contraseña=input("Entre la contraseña")
texto=funciones.validar_usuario(nombre,apellido,nombre_usuario,contraseña)
print(texto)