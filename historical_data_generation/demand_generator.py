import csv
import datetime
import random
import scipy
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from tools import node_parser
import numpy as np
import pandas as pd

def weather_quality(data):
    day_of_week = datetime.datetime(int(data[0]),int(data[1]),int(data[2])).weekday()

    quali = (float(data[3]) - float(data[5])*5 - float(data[6])*5 - float(data[7])*5) / (max(float(data[3]), float(data[5])*5, float(data[6])*5, float(data[7]))+1)

    return (day_of_week, quali)

def gen_demand(day_of_the_week, weather, tourism, size, parking, population):
    day_of_the_week = day_of_the_week % 7 + 1
    week_list=[random.randint(13,19),
               random.randint(9,15),
               random.randint(9,15),
               random.randint(10,16),
               random.randint(19,25)]
    week_list.append(100-sum(week_list))
    week_list.append(0)


    population = abs(population)
    population = population*week_list[day_of_the_week -1]/100
    population = population*(abs(weather)+0.1)

    if 0.8 > weather >= 0.5:
        tourism = tourism / 2
    elif 0.5 > weather >= 0.3:
        tourism = tourism / 4
    elif weather < 0.3:
        tourism = 0

    result = population + (population*tourism)/10
    if result < 0:
        print("population: ", population)
        print("tourism: ", tourism)
        print("result: ", result)
    return result



def demand_for_shops(n_days):
    node_data = node_parser.parse_node_parameters("data/out/node_parameters.txt")
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
        node_data_numerical.append((tourism.get(node[2]), size.get(node[0]), parking.get(node[1]), int(round(float(node[3])))))

    with open("data/in/weather_data.csv") as csvfile:
        shops_matrix = np.zeros((len(node_data),n_days), np.int64)
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
                demand = gen_demand(quali[0],quali[1],node[0], node[1], node[2], node[3])
                if demand < 0:
                    print("wtf ", demand)
                shops_matrix[i][day_count] = abs(int(round(demand)))
                day_count+=1
                # if day_count == n_days:
                #     break
        # print(shops_matrix)
        return shops_matrix

    #print(list_of_days)
    # for rec in list_of_days:
    #     demands.append(gen_demand(rec[0], rec[1], rec[2], rec[3], rec[4]))
    # print(demands)
    #plt.hist(demands)



# result = demand_for_shops(1000)
# print(result)

# results = demand_for_shops(70)
# n = 2
# print(results[n])
# # plt.hist(results[0][0])
# # plt.show()
# a = results[n]
# print(a)
# plt.plot(a, 'o')
# plt.show()

# SIZE, PARKING, TOURISM, WEATHER, EVENT, DAY OF THE WEEK