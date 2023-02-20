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

import random

#imprimri funciones de random
print(dir(random))

#numero aleatorio entr 0 y 0.99999
x=random.random()
print(x)

#numero alaeatorio entre 10 y 99
y=random.randint(10,100)
print(y)

#elige aleatotiamente un elemento de la lista
frutas=["manzanas","platano","kiwi"]
z=random.choice(frutas)
print(z)