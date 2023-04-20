a=2
b=0
try:
    print(a/b)
except ZeroDivisionError:
    print("error de division por 0")
except Exception as e:
    print("otros errores")
    print(e)
finally:
    print("siempre se ejecuta")
print("Continua el programa") 

""" try:
    f=open("abc1.txt")
    print("archivo abierto")
except Exception as e:
    print("Error al abrir el archivo")
    #cogiendo el mensaje de la excepcion
    print(e)
finally:
    print("siempre se ejecuta")

print("Continuamos") """

