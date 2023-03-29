#creacion del diccionario
acciones={"AENA.MC":143.75,"BBVA.MC":6.34,"REP.MC":14.22,"SAN.MC":3.324}
print(acciones)

#imprimir valor de un elemento del diccionario
print(acciones["BBVA.MC"])

#insertar
acciones.update({"OHLA.MC":0.518})
acciones.update({"ANE.MC":34.32})
acciones.update({"TEF.MC":3.811})

print(acciones)

#suma los valores
suma=0
#coger solo los valores
for valor in acciones.values():
   suma +=valor
print(suma)


suma1=0
#coge claves y valores
for key,valor in acciones.items():
    if key !="SAN.MC":
      suma1 += valor
print(suma1)



temperaturas={"ENE":12,"FEB":13,"MAR":15,"ABR":16,"MAY":19,"JUN":22,"JUL":24,"AGO":24,"SEP":23,"OCT":20,"NOV":16,"DIC":13}
print(temperaturas)
suma2=0
for v in temperaturas.values():
  suma2=suma2+v
print(suma2/12)
#actualizar
temperaturas.update({"ABR":35})
print(temperaturas)
print(temperaturas["ABR"])
#coge solo claves
for key in temperaturas.keys():
  print(key)
