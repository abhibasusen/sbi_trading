# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:19:04 2018

@author: ABHIBASU SEN
Special thanks to Sentdex Channel in YouTube. He did it for TSLA in US stock market and I did it for SBIN in NSE
"""

import pandas
import matplotlib
from matplotlib import style

style.use('ggplot')

pnb=pandas.read_csv("sbi1.csv", parse_dates=True, index_col=0)
pnb['100ma']=pnb['Close'].rolling(window=100,min_periods=0).mean()
pnb['20ma']=pnb['Close'].rolling(window=20,min_periods=0).mean()
print(pnb.head())
ax1=matplotlib.pyplot.subplot2grid((9,1),(0,0),rowspan=5,colspan=1)
ax2=matplotlib.pyplot.subplot2grid((9,1),(7,0),rowspan=5,colspan=1,sharex=ax1)
ax1.plot(pnb.index,pnb['Close'])
ax1.plot(pnb.index,pnb['100ma'])
ax1.plot(pnb.index,pnb['20ma'])
ax2.bar(pnb.index,pnb['Volume'])
matplotlib.pyplot.show()
