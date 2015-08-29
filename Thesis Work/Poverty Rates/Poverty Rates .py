
# coding: utf-8

# In[102]:

import pandas as pd
import pylab
import xlrd
import csv
import us
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
from IPython.lib.pretty import pprint
from pandas import *
from pylab import *
from tabulate import tabulate
# Enable inline plotting
get_ipython().magic(u'matplotlib inline')


# In[146]:

states = us.states.STATES
statesDf = pd.DataFrame(data = states, columns=['States'])

statesDf.head()
# read in data
countydata = read_csv('data/CountyPovertRates.csv')
citydata = read_csv('data/City_PovertRates.csv')
statedata = read_csv('data/State_PovertRates.csv')
metrodata = read_csv('data/Metro_PovertRates.csv')

#print('--------------')
countydata = pd.DataFrame(countydata, columns=['Geographic Area', 'Percent','Margin of Error','State'])
countydata.rename(columns={'Geographic Area': 'County', 'Percent':'Percent','Margin of Error':'Margin_of_Error'}, inplace=True)
#print countydata.head()
#print('--------------\n')
citydata = pd.DataFrame(citydata, columns=['Geographic Area', 'Percent','Margin of Error','State'])
citydata.rename(columns={'Geographic Area': 'City', 'Percent':'Percent','Margin of Error':'Margin_of_Error'}, inplace=True)
#print citydata.head()
#print('--------------\n')

statedata = pd.DataFrame(statedata, columns=['Geographic Area', 'Percent','Margin of Error'])
statedata.rename(columns={'Geographic Area': 'State', 'Percent':'Percent','Margin of Error':'Margin_of_Error'}, inplace=True)
#print statedata.head()

#print('--------------')
metrodata = pd.DataFrame(metrodata, columns=['Geographic Area', 'Percent','Margin of Error'])
metrodata.rename(columns={'Geographic Area': 'Metro_Area', 'Percent':'Percent','Margin of Error':'Margin_of_Error'}, inplace=True)
#print metrodata.head()


# In[148]:

topCounty = countydata.groupby('Percent').max()
topCounty = pd.DataFrame(topCounty.tail(10)[::-1])
bottomCounty = countydata.groupby('Percent').max()
bottomCounty = bottomCounty.head(10)
countyheaders = ['PERCENT', 'COUNTY','ERROR','STATE']
print('Top Ten COUNTIES Percentage of People Below Poverty Level')
print('_______________________________________________________')
print tabulate(topCounty,countyheaders)
print ('\n')
print('Bottom Ten COUNTIES Percentage of People Below Poverty Level')
print('__________________________________________________________')
print tabulate(bottomCounty,countyheaders)


# In[117]:

topCity = citydata.groupby('Percent').max()
topCity = pd.DataFrame(topCity.tail(10)[::-1])
bottomCity = citydata.groupby('Percent').max()
bottomCity = pd.DataFrame(bottomCity.head(10))
cityheaders = ['PERCENT', 'CITY','ERROR','STATE']
print('Top Ten Cities Percentage of People Below Poverty Level')
print('_______________________________________________________')
print tabulate(topCity,cityheaders)
print ('\n')
print('Bottom Ten Cities Percentage of People Below Poverty Level')
print('__________________________________________________________')
print tabulate(bottomCity,cityheaders)


# In[118]:

topState = statedata.groupby('Percent').max()
topState = pd.DataFrame(topState.tail(10)[::-1])
bottomState = statedata.groupby('Percent').max()
bottomState = pd.DataFrame(bottomState.head(10))
stateheaders = ['PERCENT', 'STATE','ERROR']
print('Top Ten STATES Percentage of People Below Poverty Level')
print('_______________________________________________________')
print tabulate(topState,cityheaders)
print ('\n')
print('Bottom Ten STATES Percentage of People Below Poverty Level')
print('__________________________________________________________')
print tabulate(bottomState,cityheaders)


# In[138]:

tls.embed("https://plot.ly/~dterrel3/89")


# In[139]:

tls.embed("https://plot.ly/~dterrel3/100")


# In[140]:

tls.embed("https://plot.ly/~dterrel3/216")


# In[144]:

tls.embed("https://plot.ly/~dterrel3/225")


# In[141]:

tls.embed("https://plot.ly/~dterrel3/230")


# In[142]:

tls.embed("https://plot.ly/~dterrel3/239")

