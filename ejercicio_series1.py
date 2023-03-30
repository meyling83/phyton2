import pandas as pd
import numpy as np
datos=np.random.randint(100,size=5)
series=pd.Series(datos)
series=pd.Series(datos,index=["A","B","C","D","E"])
print(series.head())
series.describe()
series.loc["A"]
series.iloc[0]
#series.iloc[500]
#series.iloc[500:504]
#series.iloc[[501,505,509]]
