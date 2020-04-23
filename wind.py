
import math
import pandas as pd

optimal = (math.pi/180) * int(input("Enter the optimal wind direction of your surf spot "))

data = pd.read_csv('D:\Surf Bunker\Pycon code\shortsands.csv')
wdir_ = data['wdir'].tolist()

def wind(optimal, wdir_):
    for spot in wdir_:
        distance = (spot - optimal)
        wind_radians = (math.cos(distance))
        print(wind_radians)
    
wind(optimal, wdir_)
    
