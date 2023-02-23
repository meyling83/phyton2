#from urllib.request import urlopen
#page=urlopen("https://github.com/")
#content=page.read()
#print(content) 

#acceder a api de cambio de moneda
#import requests
#currency="eur"
#basecurrency="aud"
#url="http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + currency + "&f=" + basecurrency + "&v=1&s=cbr"
#resp=requests.get(url)
#print(resp.text)
#print(resp.json())

#genera un identificador unico
#import uuid
#print ("El UUID uuid1() es: ",end="")
#print(uuid.uuid1())

#import turtle
#myTurtle=turtle.Turtle()
#myWin=turtle.Screen()
#for i in range(4):
    #myTurtle.forward(20)
    #myTurtle.right(90)
#myWin.exitonclick()

#acceder a api de cambio de moneda
#import requests

#url="http://jsonplaceholder.typicode.com/posts"
#resp=requests.get(url)
#print(resp.text)
#print(resp.json())

#import random

#imprimri funciones de random
#print(dir(random))

""" #numero aleatorio entr 0 y 0.99999
x=random.random()
print(x)

#numero alaeatorio entre 10 y 99
y=random.randint(10,100)
print(y)

#elige aleatoriamente un elemento de la lista
frutas=["manzanas","platano","kiwi"]
z=random.choice(frutas)
print(z) """

#bucle infinito imprimiendo hola
#while True:
    #print("hola")

#imprime hola 0, hola 1.... hasta hola 9
""" i=0
while i<10:
    print("hola"+str(i))
    i=i+1


#imprime hola 10, hola 9.... hasta hola 1
i=10
while i>0:
    print("hola"+str(i))
    i=i-1 


i=10
while i>0:
    if i==5:
        print("i es 5")
        break
    print("hola"+ str(i))
    i=i-1
print("fin de bucle") 

#ejemplo de else, si no cumple la condicion de parada del ciclo, va al else
i=10
while i>0:
    print("hola"+str(i))
    i=i-1
else:
    print("else")

# ejemplo de ciclo para que el programa pida entrada al usuario minetras la entrada sea S, si es N, sale del ciclo
accion=input("Quieres continuar S/N")
while accion=="s":
    print("haciendo bucle")
    accion=input("quieres continuar S/N")
print("fin de programa") """

#impirme los numeros del 1 al 9
""" i=1
while i<10:
    print(i)
    i+=1 """

#suma el numero introducido al total, minetras el total sea menor que 100
""" total=0
while total<100:
    num=int(input("Introducir un numero:"))
    total=total+num
print("el total es ", total) """

#contando desde 100 hasta 50
""" i=100
while i>=50:
    print(f"i con valor {i} es mayor o igual que 50.")
    i=i-1 """

#imprimir del 0 al 99 sin imprimir 10,20,30,40,50,60,70,80,90,
""" for i in range(100):
    if i not in(10,20,30,40,50,60,70,80,90):
        print(i)"""

#imprimir del 0 al 99 sin imprimir 10,20,30,40,50,60,70,80,90,
""" i=0 
while i<100:
    if i not in(10,20,30,40,50,60,70,80,90):
        print(i)
    i+=1 """

#genera numero aleatorio, si es 15, imprime es 15!!!!
""" import random

x=random.randint(12,18)
if x==15:
    print("es 15!!!!!") """

#genera valor aleatorio de la lista de estudiantes, si es maria o juan imprime "maria y juan no estan em clases"
#si es asier o jon, imprime "asier y jon si estan en clases"
""" import random
estudiantes=("jon","maria","juan","asier")

estudiante=random.choice(estudiantes)
if estudiante=="maria" or estudiante=="juan":
    print("maria y juan no estan em clases")
elif estudiante=="asier" or estudiante=="jon":
    print("asier y jon si estan en clases") """

#pregunta al usuario su contraseña y que la repita, mientras no coincidan las contraseñas sigue pidiendo que la repita
""" password=input("Introduce tu contraseña:")
repPassword=input("Introduce de nuevo tu contraseña:")
while password!=repPassword:
    repPassword=input("Introduce de nuevo tu contraseña:")
print("muy bien las contraseñas coinciden") """

""" while True:
    pw1=input("Introduce tu contraseña:")
    pw2=input("Introduce de nuevo tu contraseña:")
    if pw1==pw2:
        print("muy bien las contraseñas coinciden")
        break

i=1
ch="*"
while i<10:
    print(ch*i)
    i=i+2 
print("--------")
i=9
while i>0:
    print(ch*i)
    i=i-2

#imprimir esterellas
cadena="*"
for i in range(5):
    print(cadena)
    cadena=cadena + "**"
print("--------")
for i in range(5):
  
    indice=len(cadena)-2
    cadena=cadena[0:indice]
    print(cadena)
   


s="    122,Python,es,64,un,777,lenguaje,222,de,55,66,programación  "
s=s.strip()
a=s.split(",")
b=[] """
""" for elemento in a:
      if not elemento.isnumeric():
         b.append(elemento)
print(b) """

# esto mismo lo puedo hacer en una sola linea con list comprehension de esta forma
#b=[i for i in a if i==""]
""" b=[i for i in a if not i.isnumeric()]
print(b)
texto_final=""
for i in b:
    #texto_final=texto_final + i + " "
    #otra forma de hacerlo, para coger los elementos de la lista y hacer un string, con los espacios
    texto_final=" ".join(str(i) for i in b)
print(texto_final)
print(texto_final.upper())
print(texto_final.lower()) """



#s="     Palabra    "
#aux=s.strip()
#s="       Palabra"
#aux=s.lstrip()

""" s="hola.mundo.como.estas"
aux=s.split(".")
aux1=" ".join(i for i in aux)
print(aux)
print(aux1) """

""" #ejemplo list comprehension. Obtiene en una lista nueva los nombres que empiecen con j
nombres=["jon","maria","juan","javier"]
nueva_lista=[nombre for nombre in nombres if nombre[0]=="j"]
print(nueva_lista)

#list comprehension devolver una lista con numeros positivos
numeros=[3,54,-12,4,-67,99,-120]
lista_positiva=[numero for numero in numeros if numero>=0]
lista_duplicar=[numero*2 for numero in numeros if numero>=0]
print(lista_positiva)

#list comprehension devolver una lista con numeros negativos
lista_negativa=[numero for numero in numeros if numero<0]
print(lista_negativa) """

""" #con un bucle
numeros=[3,54,-12,4,-67,99,-120]
lista_positiva=[]
lista_negativa=[]
for numero in numeros:
    if numero>=0:
        lista_positiva.append(numero)
    else:
        lista_negativa.append(numero)

print(lista_positiva) 
print(lista_negativa) 
"""

""" 
#reemplazar
texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."
texto=texto.replace("Pitón","Python")
texto=texto.replace("difícil","facil")
texto=texto.replace("1960","1990")
texto=texto.replace("Bill Gates","Guido van Rossum")
 
print(texto)

texto = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil   "
#cantidad de veces que aparece python en el texto
cantidad=texto.lower().count("python")

#numero del caracter en el que encuentra python en el texto
primera_ocurrencia=texto.lower().find("python")

#segunda ocurrencia. me quedo con una subcadena a partir de la primera ocurrencia de python, para encontrar donde esta python en la subcadena, y sumo la longitud que le quite a la subcadena
segunda_ocurrencia=texto[primera_ocurrencia+1:len(texto)-1].lower().find("python") + primera_ocurrencia+1

print(cantidad)
print(primera_ocurrencia)
print(segunda_ocurrencia)

#buscar si codigo esta en el texto
if "código" in texto:
    print("esta")
else:
    print("no esta")

#reemplazar
#texto=texto.replace("Python","PYTHON")
print(texto)

#quitar espacios al inicio y al final
texto=texto.strip()
print("X"+texto+"X")

#convierte mayusculas a minusculas y viceversa
texto=texto.swapcase()
print(texto)
 """

#separa los nombres de los dominios
""" 
#devuelve un texto con nuevos correos
nombres = ("maria", "jon", "david")
texto=",".join(nombre+"@nazaret.eus" for nombre in nombres)
print(texto) """

#otra via de la segunda ocurrencia
""" texto = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil   "
primera_ocurrencia=texto.lower().find("python")
longitud=len("python")
segunda_ocurrencia=texto.lower().find("python",primera_ocurrencia+longitud,len(texto)-1)
print(segunda_ocurrencia) """

""" emails = ["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]
nombres=""
dominios=""
for email in emails:
    nombre,dominio=email.split("@")
    if "." in nombre:
        aux1=nombre.split(".")
        nombre_completo=" ".join(i for i in aux1)
    else:
        nombre_completo=nombre
    nombres=nombres+ "," + nombre_completo
    if dominio not in dominios:
       dominios=dominios + "," + dominio
      
print(nombres)
print(dominios)
 """

