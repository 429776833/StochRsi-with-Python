#学习用貌似效果不行
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/Alper Torun/Desktop/kişisel gelişim/yazılım/Python/proje geliştirme/4-fiyat tahmin/AAPL.csv")
a=df.iloc[:,4]
b=df.iloc[:,0]
b
df=pd.concat([b,a],axis=1)
df
#ema olusturma
def EMA(data,period=20,column="Close"):
    return data[column].ewm(span=period,adjust=False).mean()
#StochRsi olusturma
def StochRSI(data,period=14,column="Close"):
    delta=data[column].diff(1)
    delta=delta.dropna()
    up=delta.copy()
    down=delta.copy()
    up[up<0]=0
    down[down>0]=0
    data["up"]=up
    data["down"]=down
    AVG_gain=EMA(data,period,column="up")
    AVG_loss=abs(EMA(data,period,column="down"))
    RS=AVG_gain/AVG_loss
    RSI= 100.0-(100.0/(1.0+RS))
    stockrsi=((RSI-RSI.rolling(period).min())/(RSI.rolling(period).max()-RSI.rolling(period).min()))
    return stockrsi
df["StochRSI"]=StochRSI(df)
#plot the data
fig,(ax1,ax2)=plt.subplots(nrows=2,sharex=True)
ax1.plot(df.index,df["Close"],color="r")
ax2.plot(df.index,df["StochRSI"],color="b",linestyle="--")
#aradaki boslugu silme
plt.subplots_adjust(hspace=.0)
ax1.grid()
ax2.grid()
plt.xticks(rotation=45)
#asiri alim 0.8 cizgisi ve asiri satim 0.2 cizgisi
ax2.axhline(0.2,color="orange")
ax2.axhline(0.8,color="orange")












