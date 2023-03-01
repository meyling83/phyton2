def validar_usuario(usuario):
    LONGITUD=6
    if len(usuario)<6:
        print("El nombre de usuario tiene que ser mayor que 5")
        return False
    else:
        return True
    """ if len(usuario)<=5:
        return "El nombre de usuario tiene que ser mayor que 5"
    elif len(contraseña)<=6:
        return "La contraseña tiene que ser mayor que 6"
    elif contraseña in lista:
        return "La contraseña no es correcta"
    else: 
        return "Bienvenido " + str(nombre).swapcase() + " " + str(apellido).swapcase() """
    
""" def validar_contraseña(contraseña):
    lista=["password","contraseña","123456"]
    LONGITUD=7
    if len(contraseña)<LONGITUD:
        print("La contraseña tiene que ser mayor que 6")
        return False
    elif contraseña in lista:
        print("La contraseña es muy facil")
        return False
    else:
        return True """