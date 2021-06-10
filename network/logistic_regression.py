import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from historical_data_generation.demand_generator import weather_quality
from solver.solver import solve_date
import csv
import datetime
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

y=np.zeros(1000)
x=np.zeros((1000,3))
with open("data/in/weather_data.csv") as csvfile:
    n_days = 1000 # num of days
    i=0
    for row in csv.reader(csvfile, delimiter=','):
        if i==0:
            i +=1
            continue
        day = datetime.datetime(int(row[0]),int(row[1]),int(row[2])).weekday()
        y[i-1] = solve_date((row[0], row[1], row[2]),100)
        x[i-1][0] = int(row[1])
        x[i-1][1] = int(row[2])
        x[i-1][2] = day
        i += 1
        if i == n_days+1:
            break
    res = np.append(x, y.reshape(1000,1), axis=1)
    pd.DataFrame(res).to_csv("data/out/network_data.csv")
print(x)
print(y)

#for i in weather
# i znowu for na x z data
# nie wiem czy moze byc dwukolumnowy
# ale wtedy na druga kolumne for z pogoda



# model = LogisticRegression(solver='liblinear', random_state=0)
# model.fit(x,y)