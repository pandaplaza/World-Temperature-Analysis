# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:53:35 2017

@author: troy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
plt.style.use('ggplot')
sb.set(style="darkgrid")

#Climate data by year and month starting from 1750. 
climate = pd.read_csv('C:\\Users\\troy\\Desktop\\Datasets\\GlobalTemperatures.csv', 
                      na_values = [''],
                       )
#Creates a list of all the unique years for iteration
years = np.unique(climate['dt'].apply(lambda x: x[:4]))




#The datafile is quite large, so we will just start by analyzing one variable:
#Land Average Temperature. We also need to clean the dataset as the format for 
#year and month is not easy to analyze.
climate['dt'] = climate['dt'].apply(lambda x: x[:4])
#climate.set_index(['dt'], inplace=True)

#Iterates through each year and finds the mean of all of the land average temp.
#for that year. Stores it in a list for easy cross-tab with years.
lat = []
for year in years:
    lat.append(climate[climate['dt'].apply(lambda x: x[:4]) == year]['LandAverageTemperature'].mean())
        
#Turns years and lat into a dataframe in order to use for seaborn plots, making the index Year
lat_df = pd.DataFrame({'Year': years, 'LAT': lat})
#lat_df.set_index(['Year'], inplace=True)

#Creates a csv out of lat_df for potential ease in future use.
lat_df.to_csv('latperyear.csv')


  
#Utilizing seaborn's factorplot, we will plot mean average land temp. by
#year. Calculation of average will simply be the average temperature for the
#entire year, rather than each month as the original data was structured.
y_years = np.arange(1800, 2016)
g = sb.factorplot(x = "Year", y = "LAT", data=lat_df, kind="strip", palette="BuPu")
g.set_xticklabels(step=50)