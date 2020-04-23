# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import pandas as pd
import mord
import math
import requests_cache
import csv

#Get data collected data with ratings
collected_data = pd.read_csv('D:\Surf Bunker\Pycon code\shortsands.csv')
wdir_ = collected_data['wdir'].tolist()

#Get forecasting data from Planet OS
url = "https://api.planetos.com/v1/datasets/meteofrance_global_ocean_forecast/point?apikey=850b2209e8fb42639cfee784f799223a&origin=dataset-details&lat=49.5&lon=-50.5&csv=true&count=50&_ga=2.267069639.852181704.1582622787-1257781974.1581510092"
planet_os = requests.get(url).content
requests_cache.install_cache(planet_os)

wind_dir = surf_data["Direction_of_wind_waves_surface"].tolist()
wind_spd = surf_data["Wind_speed_surface"].tolist()
swell_p = surf_data["Mean_period_or_primary_swell_waves"].tolist()
swell_d = surf_data["Direction_of_primary_swell_waves"].tolist()
swell = surf_data["Significant_height_of_primary_swell_waves"].tolist()

print wind_dir
#Converting the wind direction variable to radians so that it can be interpreted in the regression
def recode_wind(wdir_):
    optimal = 90
    for wdir_ in list:
        distance = (wdir_ - optimal)
        wind_radians = (math.cos(distance))
        return(wind_radians)
        
collected_data['recode_wind'] = collected_data.wdir.apply(recode_wind)    
print(collected_data.head)        

#Here is the actual regression
forecast = mord.LogisticIT()
forecast.fit(collected_data[['swell','wspd','period']], collected_data['rating'])
forecast.predict([['swell', 'wind_spd','swell_p']])
forecast.describe
print forecast.coef_
