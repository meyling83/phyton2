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

if __name__=="__main__":
   compra()
"""     d=float(input("Entre la distancia"))
    t=float(input("Entre el tiempo"))
    v=velocidad(d,t)
    print(f"La velocidad es {v:.2f}")  """
