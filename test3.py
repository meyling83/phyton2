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




