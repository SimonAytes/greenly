import pandas as pd


carbon = pd.read_csv("~/hsi project/carbon-footprint-travel-mode.csv")
col_names = ['Transportation Type', 'GHG emissions (gCO2e/km)']
carbon_df = pd.DataFrame(0, index= range(0,3), columns = col_names)

carbon
car_sum = []

for i in range(0,len(carbon),1):
    if 'petrol' in carbon['Entity'][i]:
        car_sum.append(carbon['GHG emissions (gCO2e/km)'][i])
        
print(car_sum)
        
carbon_df.loc[0,'Transportation Type'] = "Car" 
carbon_df.loc[0,'GHG emissions (gCO2e/km)'] = sum(car_sum)/len(car_sum) 

carbon_df.loc[1,'Transportation Type'] = "Bus" 
carbon_df.loc[1,'GHG emissions (gCO2e/km)'] = carbon.loc[1,'GHG emissions (gCO2e/km)']

#Adding scooter info directly to the dataframe
carbon_df.loc[2,'Transportation Type'] = "Scooter" 
carbon_df.loc[2,'GHG emissions (gCO2e/km)'] = 202



carbon_df.to_csv('~/hsi project/CO_unit_measures.csv',index=False)
carbon_df