
import pandas as pd


carbon = pd.read_csv("~/hsi project/carbon-footprint-travel-mode.csv")
col_names = ['Transportation Type', 'GHG emissions (gCO2e/km)','Green Score']
carbon_df = pd.DataFrame(0, index= range(0,3), columns = col_names)

carbon
car_sum = []

for i in range(0,len(carbon),1):
    if 'petrol' in carbon['Entity'][i]:
        car_sum.append(carbon['GHG emissions (gCO2e/km)'][i])
        
print(car_sum)
car_max = max(car_sum)
        
carbon_df.loc[0,'Transportation Type'] = "Car-average" 
carbon_df.loc[0,'GHG emissions (gCO2e/km)'] = sum(car_sum)/len(car_sum)
carbon_df.loc[0,'Green Score'] = 100- ((sum(car_sum)/len(car_sum))/car_max)*100

carbon_df.loc[1,'Transportation Type'] = "Car-max" 
carbon_df.loc[1,'GHG emissions (gCO2e/km)'] = car_max
carbon_df.loc[1,'Green Score'] = 0

carbon_df.loc[2,'Transportation Type'] = "Bus" 
carbon_df.loc[2,'GHG emissions (gCO2e/km)'] = carbon.loc[1,'GHG emissions (gCO2e/km)']
carbon_df.loc[2,'Green Score'] =100 - (carbon.loc[1,'GHG emissions (gCO2e/km)']/car_max)*100

#Adding scooter info directly to the dataframe
carbon_df.loc[3,'Transportation Type'] = "Scooter" 
carbon_df.loc[3,'GHG emissions (gCO2e/km)'] = 202
carbon_df.loc[3,'Green Score'] = 100 - (202/car_max)*100

carbon_df.loc[4,'Transportation Type'] = "Car-pool-1person" 
carbon_df.loc[4,'GHG emissions (gCO2e/km)'] = (sum(car_sum)/len(car_sum))/4
carbon_df.loc[4,'Green Score'] = 100- (((sum(car_sum)/len(car_sum))/4)/car_max)*100



carbon_df.to_csv('~/hsi project/CO_unit_measures.csv',index=False)
carbon_df