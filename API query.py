# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:06:09 2020

@author: matth_2o0mb3d
"""
import requests


url = "https://api.planetos.com/v1/datasets/meteofrance_global_ocean_forecast/point?apikey=850b2209e8fb42639cfee784f799223a&origin=dataset-details&lat=49.5&lon=-50.5&csv=true&count=50&_ga=2.267069639.852181704.1582622787-1257781974.1581510092"
querystring = {"apikey":"{850b2209e8fb42639cfee784f799223a}"}

response = requests.request("GET", url, params=querystring)
result = response.json()
print result


