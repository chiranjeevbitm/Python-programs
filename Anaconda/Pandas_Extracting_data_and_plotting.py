"""
Created on Sat Dec 30 19:07:39 2017

@author: Chiranjeev
"""

import  pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
country = pd.read_csv(r"C:\Users\Chiranjeev\Downloads\UN-data.csv",usecols=['Nation','HDI','CO2','Life'])
#df1=country.head()
#df2=country.tail(10)
df = country.head(15)
print(df)
#print(df1)
#print(df2)
#df.irow(1)
#df.set_index('number',inplace = True)
#sd = df.reindex(coulmns = ['2011','2012'])
#db=sd.diff(axis=1)
df.CO2.hist()
#print df.describe()
#print country.head()
#print country.tail(10)
df.plot()
plt.show()
df.HDI.plot()
#print len(df)
df.Life.hist()
df.HDI.hist()


