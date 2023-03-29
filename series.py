import pandas as pd
datos={"AENA.MC":143.75,"BBVA.MC":6.34,"REP.MC":14.22,"SAN.MC":3.324}
#convierte el diccionario en una serie
series=pd.Series(datos)
print(series)
series.loc["REP.MC"]
datos1=[45,23,7,5,8,9,10]
#convierte la lista en una serie
series1=pd.Series(datos1)
print(series1)
#valor del indice 4
series1.loc[4]
#cantidad
print(series1.count())
#suma
print(series1.sum())
#dos menores
print(series1.nsmallest(n=2))
#el mayor
print(series1.nlargest(n=1))
#promedio
print(series1.mean())
#estadisticas
series1.describe()
#dos primeros
series1.head(2)
#ultimo
series1.tail(1)
