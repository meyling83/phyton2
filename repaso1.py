import random
import pandas as pd
#programa para calcular la velocidad dado la distancia y el tiempo introducidos por el usuario
def velocidad(d,t):
    return d/t
def distancia(v,t):
    return v*t
def tiempo(d,v):
    return d/v



#repetir x veces
def repetirXveces(veces):
    texto=""
    for i in range(veces):
      if i!=5 and i!=6:
        texto=texto + "," + str(i)
      
    print(texto)

#dias semana
def diasSemana():
   dias=("lunes","maretes","miercoles","jueves","viernes","sabado","domingo")
   print(dias[0])
   #print(dias[-1])
   print(dias[len(dias)-1])

#impar
def impar():
    a = 1
    while a <= 20:
        if a%2!=0:
            print(a)
        a=a+1
#numeros 100
def numeros():
   for i in range(100,0,-10):
      print(i)

#lista de compra
lista=["manzanas","leche","papel de cocina"]
def compra():
   
   accion=input("Entre M si quiere mostrar la lista o A si quiere añadir elementos")
   if accion.upper()=="M":
      for i in lista:
         print(i)
   elif accion.upper()=="A":
       elemento=input("Entre el elmento a añadir")
       lista.append(elemento)
       for i in lista:
          print(i)

def imparOtra():
   numero=int(input("Entre un numero"))
   if(numero%2!=0):
      return str(numero) + "es impar"
   else:
      return str(numero) +  " es par"

def suspendido():
   lista=[5,6,4,9,9,10,5]
   #otra via mejor
   print(any(nota<5 for nota in lista))
"""    for i in lista:
      if i<5:
         print("Alguien suspendio")
         break
 """
jon=(True,False,False,True,False)
maria=(True,True,True,True,True)
#si todos son verdaderos devyelve verdadero, sino falso
print(all(jon))
print(all(maria))
#    for i in maria:
#       if not i:
#          print("false")
#          break
      


def reemplazar(texto):
    texto= texto.replace("Pitón","Python")
    return texto
def sumar(numero1,numero2,numero3):
   return numero1+numero2+numero3

def validarProducto(nombre,precio,cantidad):
   if nombre[0].isupper() and precio>10 and cantidad>=1 and cantidad<=100:
      return True
   else:
      return False
      

class Producto:
   def __init__(self,nombre,precio,cantidad):
       self.nombre=nombre
       self.precio=precio
       self.cantidad=cantidad
       
   def hola(self):
      print(f"Soy un producto {self.nombre}")

class Libro(Producto):
   def __init__(self,nombre,precio,cantidad,paginas):
      super().__init__(nombre,precio,cantidad)
      self.paginas=paginas
   def hola(self):
      print(f"Soy un libro {self.nombre}")
      
   

if __name__=="__main__":
  import pandas as pd
""" df=pd.read_csv("https://raw.githubusercontent.com/kromerm/adfdataflowdocs/master/sampledata/moviesDB2.csv")
df = df.rename(columns={'movies': 'id', 'Title': 'titulo', 'genresgenregenre':'tipo', 'YEAR':'año', 'Rating':'puntuacion'})
df.head() """
"""    accion=""
   while accion!="p":
       v2=random.randint(0,10)
       print(v2)
       accion=("Entre p si quiere parar") """
"""    v1=random.random()
   print(v1) """
  
  
"""    coche={
      "brand":"Ford",
      "modelo":"Mustang",
      "año":1964
   }
   coche.update({"decapotable":False})
   print(coche)
   for key,value in coche.items():
      if(type(value)!=int):
        print(key,value) """
      
"""     v= validarProducto("Camiseta",12.99,100)
    print (v) """
""" p=Producto("Camiseta",12,100)
     p.hola()
     l=Libro("Edad de Oro",12.88,120,300)
     l.hola() """
"""    n1=float(input("Entre un numero"))
   n2=float(input("Entre un numero 1"))
   n3=float(input("Entre un numero 2"))
   print(sumar(n1,n2,n3)) """
"""     texto="Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón es fácil de usar."
    texto=reemplazar(texto)
    print(texto.upper())
    lista=texto.split(" ")
    lista.sort()
    for i in lista:
       print(i) """
"""     for i in lista:
       print(i[0]) """
    
      
"""     d=float(input("Entre la distancia"))
    t=float(input("Entre el tiempo"))
    v=velocidad(d,t)
    print(f"La velocidad es {v:.2f}")  """
