import pandas as pd
acciones={"SAN":[3,4,7,3],"REP":[14,16,6,12],"IBM":[192,150,120,200]}
df=pd.DataFrame(acciones)
print(type(df))

df.head()
df.describe()
df.tail()
#filas 1 y 3
df.loc[[1,3]]
#filas entre 20 y 30
df.loc[20:30]
#filtro "REP">10. Muestra todas las columnas, solo las filas donde el valor es mayor que 10
df.loc[df["REP"]>10]
#filtro, muestra las filas con valor igual a 16, solo la columna "REP"
df.loc[df["REP"]==16,"REP"]
#filtro, muestra las filas con valor igual a 16, solo la columna "IBM" y REP"
df.loc[df["REP"]==16,["IBM","REP"]]
