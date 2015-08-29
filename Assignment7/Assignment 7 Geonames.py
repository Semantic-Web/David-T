
# coding: utf-8

# In[352]:

import pandas as pd
import pylab
import matplotlib.pyplot as plt
import geonamescache
import pprint
from geopy.geocoders import Nominatim
from geopy.geocoders import get_geocoder_for_service
from IPython.lib.pretty import pprint
from pandas import *
from pylab import *
get_ipython().magic(u'matplotlib inline')
import pandas
import numpy
import matplotlib.pyplot


# In[353]:

# read in data Top 10 Largest Schools in Florida
data = read_csv('datasets/Top_10_LargestSchools_In_Florida.csv',)
data.head(10)


# In[354]:

geolocator = Nominatim()
rank1 = geolocator.geocode('Miami Dade College')
rank2 = geolocator.geocode('University of Central Florida')
rank3 = geolocator.geocode('University of Florida')
rank4 = geolocator.geocode('Florida International University')
rank5 = geolocator.geocode('University of South Florida')
rank6 = geolocator.geocode('Florida State University')
rank7 = geolocator.geocode('Valencia Community College')
rank8 = geolocator.geocode('Broward College')
rank9 = geolocator.geocode('Florida Atlantic University')
rank10 = geolocator.geocode('Nova Southeastern University')
devider=('-------------------------------------------------------------------------------------------')
print("----------Printing the Addresses of the Top 10 Highest Populated Colleges in Florida----------)")
print('\nMiami Dade College\n---------------')
print(rank1.address)
print(devider)
print('\nUniversity of Central Florida\n-----------------------')      
print(rank2.address)
print(devider)
print('\nUniversity of Florida\n---------------------------')
print(rank3.address)
print(devider)
print('\nFlorida International University\n----------------------------------')
print(rank4.address)
print(devider)
print('\nFlorida International University\n----------------------------------')
print(rank5.address)
print(devider)
print('\nFlorida State University\n------------------------------------')
print(rank6.address)
print(devider)
print('\nValencia Community College\n---------------------------------')
print(rank7.address)
print(devider)
print('\nBroward College\n---------------------------')
print(rank8.address)
print(devider)
print('\nFlorida Atlantic University\n------------------------------------')
print(rank9.address)
print(devider)
print('\nNova Southeastern University\n-------------------------------------')
print(rank10.address)
print(devider)


# In[355]:

top10 = data
labels = ('Nova Southeastern University', 'Florida Atlantic University', 'Broward College', 
                           'Valencia Community College', 'Florida State University', 'University of South Florida',
                           'Florida International University','University of Florida','University of Florida',
                           'Unviversity of Central Florida','Miami Dade College')
barChart = top10.plot(kind='bar',title='Top Ten Highest Ranked Populated Colleges in Florida', width=.4)
barChart.set_ylabel('Population')
barChart.set_xlabel('Florida Colleges')
barChart.legend(['Total', 'Poplation'],loc=9,ncol=4)
barChart.set_xticklabels(labels,ha='right',rotation=25 )
plt.show()
barChart.plot()

# Add some margin to the bottom so the labels aren't cut-off.
matplotlib.pyplot.subplots_adjust(bottom=_BOTTOM_MARGIN)



# In[ ]:



