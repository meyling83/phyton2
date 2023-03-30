import requests
url="https://www.donostia.eus/datosabiertos/recursos/camaras-trafico/camarastraficocas.json"
resultado=requests.get(url)
camaras=resultado.text
#print(camaras)
print(type(camaras))
lista_camaras=resultado.json()
print(type(lista_camaras))
for i in lista_camaras:
  #print(type(i))
  if i["Nombre"]=="Ondarreta":
    print("!!!MI BARRIO ES: " + i["Nombre"] + "!!!!!!!!")
  else:
    print(i["Nombre"])
  print("Longitud: " + i["Longitud"])
  print("Latitud: " + i["Latitud"])
