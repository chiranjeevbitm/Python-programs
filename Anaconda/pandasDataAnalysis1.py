# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 20:47:29 2018

@author: Chiranjeev
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
#style.use('fivethirtyeight')
style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats)
#print (df)
#df.set_index('Day',inplace=True)
#print(df.head())
#print(df.tail())
#print(df.tail(2))

print(df.Visitors.tolist())
print(np.array(df[['Bounce Rate','Visitors']]))
df['Visitors'].plot()
#
#print(df['Visitors'])
#df['Visitors'].plot()
#plt.show()
#df.plot()
#plt.show()
#print(df[['Visitors','Bounce Rate']])
