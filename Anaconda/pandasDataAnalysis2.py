# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 22:39:00 2018

@author: Chiranjeev
"""

import pandas as pd

df = pd.read_csv(r"C:\Users\Chiranjeev\Desktop\Pandas\ZILLOW-N4009_ZHVIMTY.csv")
#print(df.head())
#df.set_index('Date',inplace=True)
#df.to_csv(r"C:\Users\Chiranjeev\Desktop\Pandas\newcsv2.csv")
#df = pd.read_csv(r"C:\Users\Chiranjeev\Desktop\Pandas\newcsv2.csv", index_col=0)
#print(df.head())
df.rename(columns={'Value':'Chiranjeev'}, inplace=True)
#print(df.head())
#df.to_html(r"C:\Users\Chiranjeev\Desktop\Pandas\newcsv2.html")
import urllib2
response = urllib2.urlopen('http://www.quandl.com/api/v1/datasets/OFDP/FUTURE_VX1.csv?&trim_start=2004-05-03&trim_end=2014-01-07&sort_order=desc')
html = response.read()