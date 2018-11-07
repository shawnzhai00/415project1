# -*- coding: utf-8 -*-
"""
MGTF 415
Project 1
Blue Group 7
"""
import pandas as pd     
import numpy as np
import json
import requests
import urllib
from datetime import datetime

# Get data from FRED

my_key="3d9da500bf6919c330cd611dd2d027f3"                             

link = 'https://api.stlouisfed.org/fred/series/observations?series_id=DPRIME&api_key=3d9da500bf6919c330cd611dd2d027f3&file_type=json&frequency=d'
f = urllib.request.urlopen(link)
raw_data = json.loads(f.read().decode("utf-8"))                                     
    
dataset=(pd.DataFrame(raw_data['observations'])[['date','value']])    
dataset=dataset.rename(index=str, columns={"value": "DPRIME"})

dataset.set_index('date', inplace=True)
dataset.to_csv('Prime_Rate.csv')

'''
'''
my_key="3d9da500bf6919c330cd611dd2d027f3"                             

link = 'https://api.stlouisfed.org/fred/series/observations?series_id=USD3MTD156N&api_key=3d9da500bf6919c330cd611dd2d027f3&file_type=json&frequency=d'
f = urllib.request.urlopen(link)
raw_data = json.loads(f.read().decode("utf-8"))                                     
    
dataset=(pd.DataFrame(raw_data['observations'])[['date','value']])    
dataset=dataset.rename(index=str, columns={"value": "LIBOR"})

dataset.set_index('date', inplace=True)
dataset.to_csv('LIBOR.csv')
'''
'''
my_key="3d9da500bf6919c330cd611dd2d027f3"                             

link = 'https://api.stlouisfed.org/fred/series/observations?series_id=MORTGAGE30US&api_key=3d9da500bf6919c330cd611dd2d027f3&file_type=json'
f = urllib.request.urlopen(link)
raw_data = json.loads(f.read().decode("utf-8"))                                     
    
dataset=(pd.DataFrame(raw_data['observations'])[['date','value']])    
dataset=dataset.rename(index=str, columns={"value": "Mortgage"})

dataset.set_index('date', inplace=True)
dataset.to_csv('Mortgage.csv')
'''
'''
my_key="3d9da500bf6919c330cd611dd2d027f3"                             

link = 'https://api.stlouisfed.org/fred/series/observations?series_id=DGS30&api_key=3d9da500bf6919c330cd611dd2d027f3&file_type=json&frequency=d'
f = urllib.request.urlopen(link)
raw_data = json.loads(f.read().decode("utf-8"))                                     
    
dataset=(pd.DataFrame(raw_data['observations'])[['date','value']])    
dataset=dataset.rename(index=str, columns={"value": "T bond"})

dataset.set_index('date', inplace=True)
dataset.to_csv('T Bond.csv')

# Get data from Bloomberg

Prime_rate=pd.read_csv('Prime_Rate.csv')
LIBOR_rate=pd.read_csv('LIBOR.csv')
Mortgage_rate=pd.read_csv('Mortgage.csv')
Tbond_rate=pd.read_csv('T Bond.csv')

# Manipulate the data
AIG_data=pd.read_csv('AIG.csv')
CX_data=pd.read_csv('CX.csv')
WMT_data=pd.read_csv('WMT.csv')

df = AIG_data.copy()
df = CX_data.copy()
df = WMT_data.copy()

## Rename the columns

AIG_data=AIG_data.rename(columns={"AIG US Equity": "Date","Last Price":"AIG"})
CX_data=CX_data.rename(columns={"CX US Equity": "Date","Last Price":"CX"})
WMT_data=WMT_data.rename(columns={"WMT US Equity": "Date","Last Price":"WMT"})

Prime_rate=Prime_rate.rename(columns={"date": "Date","value":"DPRIME"})
LIBOR_rate=LIBOR_rate.rename(columns={"date": "Date"})
Mortgage_rate=Mortgage_rate.rename(columns={"date": "Date"})
Tbond_rate=Tbond_rate.rename(columns={"date": "Date"})

# Change to the numeric values
Prime_rate['DPRIME']=pd.to_numeric(Prime_rate['DPRIME'],errors='coerce')
LIBOR_rate['LIBOR']=pd.to_numeric(LIBOR_rate['LIBOR'],errors='coerce')
Mortgage_rate['Mortgage']=pd.to_numeric(Mortgage_rate['Mortgage'],errors='coerce')
Tbond_rate['T bond']=pd.to_numeric(Tbond_rate['T bond'],errors='coerce')
AIG_data['AIG']=pd.to_numeric(AIG_data['AIG'],errors='coerce')
CX_data['CX']=pd.to_numeric(CX_data['CX'],errors='coerce')
WMT_data['WMT']=pd.to_numeric(WMT_data['WMT'],errors='coerce')

'''
 Question 2C
'''
# Find the number of NaNs or null values in each column.

Prime_rate.isna().sum()
LIBOR_rate.isna().sum()
Mortgage_rate.isna().sum()
Tbond_rate.isna().sum()
AIG_data.isna().sum()
CX_data.isna().sum()
WMT_data.isna().sum()

# Find empty string

print(Prime_rate[Prime_rate==""].count())
print(LIBOR_rate[LIBOR_rate==""].count())
print(Mortgage_rate[Mortgage_rate==""].count())
print(Tbond_rate[Tbond_rate==""].count())
print(AIG_data[AIG_data==""].count())
print(CX_data[CX_data==""].count())
print(WMT_data[WMT_data==""].count())

'''
 Question 2d
'''

## If more than 40% of any column is NaNs or empty strings or non-float values, drop that column.

AIG_data=AIG_data.drop(["Official Closing Price"],axis="columns")
CX_data=CX_data.drop(["Official Closing Price"],axis="columns")
WMT_data=WMT_data.drop(["Official Closing Price"],axis="columns")

'''
 Question 2e
'''

# use interpolate() to replace the NaNs or empty strings 

Prime_rate=Prime_rate.interpolate("linear")
LIBOR_rate=LIBOR_rate.interpolate("linear")
Tbond_rate=Tbond_rate.interpolate("linear")
AIG_data=AIG_data.interpolate("linear")
CX_data=CX_data.interpolate("linear")
WMT_data=WMT_data.interpolate("linear")

'''
 Question 2f
'''
## Print the number of NaNs in each column

Prime_rate.isna().sum()
LIBOR_rate.isna().sum()
Mortgage_rate.isna().sum()
Tbond_rate.isna().sum()
AIG_data.isna().sum()
CX_data.isna().sum()
WMT_data.isna().sum()

## Print the number of empty strings in each column

print(Prime_rate[Prime_rate==""].count())
print(LIBOR_rate[LIBOR_rate==""].count())
print(Mortgage_rate[Mortgage_rate==""].count())
print(Tbond_rate[Tbond_rate==""].count())
print(AIG_data[AIG_data==""].count())
print(CX_data[CX_data==""].count())
print(WMT_data[WMT_data==""].count())

'''
 3.Plot the following with appropriate labels. 
 3a Walmart - Date vs WMT
'''

df = WMT_data.copy()
df = df[(df['Date'] >= 2007) & (df['Date'] <= 2009)]

plt.plot(WMT_data[:265*5]['Date'].values, usd_data[:265*5]['USD Index'].values,linewidth=0.5)
plt.xticks(np.arange(0,265*6,265),[str(i)[:4] for i in list(usd_data[:265*6]['date'].values)[::265]], rotation=90)
plt.xlabel('Date')
plt.ylabel('USD Rate')
plt.title('USD Rate before Cleaning')
plt.show()