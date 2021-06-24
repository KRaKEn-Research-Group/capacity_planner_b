import pandas as pd
import numpy as np
import csv 

n_days = 5000
x=np.zeros((n_days,1))
with open("data/in/weather_data.csv") as csvfile:
    # num of days
    i=0
    for row in csv.reader(csvfile, delimiter=','):
        if i==0:
            i +=1
            continue
        quali = (float(row[3]) - float(row[5])*5 - float(row[6])*5 - float(row[7])*5) / (max(float(row[3]), float(row[5])*5, float(row[6])*5, float(row[7]))+1)
        x[i-1][0] = quali
        i += 1
        if i == n_days+1:
            break
pd.DataFrame(x).to_csv("data/out/network_data_weather_quali.csv")
