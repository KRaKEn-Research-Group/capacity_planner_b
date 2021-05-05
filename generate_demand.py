import csv
import datetime
import random
import scipy
import matplotlib.pyplot as plt
import node_parser
import numpy as np
import pandas as pd

def weather_quality(data):
    day_of_week = datetime.datetime(int(data[0]),int(data[1]),int(data[2])).weekday()

    quali = (float(data[3]) - float(data[5])*5 - float(data[6])*5 - float(data[7])*5) / (max(float(data[3]), float(data[5])*5, float(data[6])*5, float(data[7]))+1)

    return (day_of_week, quali)

def gen_demand(day_of_week, weather, location, size, parking):
    result = ((1 + 0.2*size) * (1/(day_of_week%7+1)) * location) + weather + parking*2
    return result

node_data = node_parser.parse_node_parameters("node_parameters.txt")
node_data_numerical = []

size = {
    "very_small": 1,
    "small": 2,
    "medium": 3,
    "big": 4,
    "very_big": 5
}

parking = {
    "no_parking": 0,
    "parking": 1,
}

tourism = {
    "low_tourism": 1,
    "medium_tourism": 2,
    "high_tourism": 3
}

for node in node_data:
    node_data_numerical.append((tourism.get(node[2]), size.get(node[0]), parking.get(node[1])))

def demand_for_shops(n_days):
    with open("weather_data.csv") as csvfile:
        shops_matrix = np.zeros((len(node_data),n_days))
        #n_days = 1000 # num of days
        data = csv.reader(csvfile, delimiter=',')
        data = list(data)
        
        for i in range(len(node_data_numerical)):
            node = node_data_numerical[i]
            day_count=0
            for day in data[1:n_days+1]:
                # if day_count==0:
                #     day_count+=1
                #     continue
                quali = weather_quality(day)
                # rand_location = random.randrange(0, 200)/100
                # rand_size = random.randint(1,5)
                # rand_event = random.choice([1,2,3])
                demand = gen_demand(quali[0],quali[1],node[0], node[1], node[2])
                shops_matrix[i][day_count] = demand
                day_count+=1
                # if day_count == n_days:
                #     break
        return shops_matrix

    #print(list_of_days)
    # for rec in list_of_days:
    #     demands.append(gen_demand(rec[0], rec[1], rec[2], rec[3], rec[4]))
    # print(demands)
    #plt.hist(demands)

result = demand_for_shops(1000)
nice = pd.DataFrame(result)
print(nice)


# SIZE, PARKING, TOURISM, WEATHER, EVENT, DAY OF THE WEEK