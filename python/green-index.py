import math
import os
import csv
import pandas as pd

def getGreenIndex(max_perc, carbon_val, distance):
    dist_km = distance / 1.6 #Convert distance to KM from Miles
    return(round((1-(carbon_val*dist_km)/(max_perc*dist_km))*100, 0))

carbon_data = pd.read_csv(open("CO_unit_measures.csv"))

max_percentile = carbon_data['GHG emissions (gCO2e/km)'].max()

green_score = getGreenIndex(max_percentile, carbon_val=52.3, distance=12.1)

print(green_score)