import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/sivabalanb/Data-Analysis-with-Pandas-and-Python/master/fortune1000.csv")
#primeros 5
#df.head()
#filtro compañia igual apple
#df.loc[df["Company"]=="Apple"]
#ultimos 5
#df.tail()
#filas 500 a 504
#df.loc[500:504]
#filas 500 a 504, columnas "Rank","Company","Sector"
#df.loc[500:504,["Rank","Company","Sector"]]
#filas 500 a 504, columnas "Company","Sector","Profits"
#df.loc[500:504,["Company","Sector","Profits"]]
#filas 500 a 504, columnas de la 0  a la 3
#df.iloc[500:504,0:3]
#filtro profits entre 14_000 y 20_000, oredenado descendentemente por profits, mostrar solo columnas
#df.loc[(df["Profits"]>=14_000) & (df["Profits"]<=20_000),["Company","Location","Profits"]].sort_values("Profits",ascending=False)
#lo mismo pero por pasos, mas facil
#df1=df.loc[(df["Profits"]>=14_000)]
#df2=df1.loc[(df["Profits"]<=20_000)]
#df3=df2.sort_values("Profits",ascending=False)
#df_final=df3[["Company","Location","Profits"]]
#df_final.head()
#grafico de barra plot.bar
df1=df.loc[(df["Sector"]=="Technology") & (df["Employees"]>100_000)].plot.bar(x="Company",y="Employees")
