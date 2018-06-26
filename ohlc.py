# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:06:21 2018

@author: ABHIBASU SEN
"""

## Special thanks to Sentdex channel in Youtube. He did that for tsla in Us market and I did it for sbi in NSE

import pandas
import matplotlib
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
style.use('ggplot')

pnb=pandas.read_csv("sbi1.csv", parse_dates=True, index_col=0)
pnb_ohlc= pnb['Close'].resample('10D').ohlc()
pnb_volume=pnb['Volume'].resample('10D').sum()
pnb_ohlc.reset_index(inplace=True)
pnb_ohlc['Date']=pnb_ohlc['Date'].map(mdates.date2num)

ax1=matplotlib.pyplot.subplot2grid((9,1),(0,0),rowspan=5,colspan=1)
ax2=matplotlib.pyplot.subplot2grid((9,1),(7,0),rowspan=5,colspan=1,sharex=ax1)
candlestick_ohlc(ax1,pnb_ohlc.values,width=2,colorup='g')
ax2.fill_between(pnb_volume.index.map(mdates.date2num),pnb_volume.values,0)

matplotlib.pyplot.show()