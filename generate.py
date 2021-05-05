import csv
import datetime
import random
import scipy
import matplotlib.pyplot as plt
import parser

def weather_quality(data):
    day_of_week = datetime.datetime(int(data[0]),int(data[1]),int(data[2])).weekday()

    quali = (float(data[3]) - float(data[5])*5 - float(data[6])*5 - float(data[7])*5) / (max(float(data[3]), float(data[5])*5, float(data[6])*5, float(data[7])))

    return (day_of_week, quali)

def gen_demand(day_of_week, weather, location, size, event):
    result = ((1 + 0.2*size) * (1/(day_of_week%7+1)) * location) + weather + event*2
    return result

node_data = parser.parse_node_parameters("node_parameters.txt")

with open("weather_data.csv") as csvfile:
    list_of_days = []
    n = 1000
    data = csv.reader(csvfile, delimiter=',')
    i=0
    for day in data:
        if i==0:
            i+=1
            continue
        quali = weather_quality(day)
        rand_location = random.randrange(0, 200)/100
        rand_size = random.randint(1,5)
        rand_event = random.choice([1,2,3])
        list_of_days.append([quali[0],quali[1],rand_location, rand_size, rand_event])
        i+=1
        if i == n:
            break

    #print(list_of_days)
    demands = []
    for rec in list_of_days:
        demands.append(gen_demand(rec[0], rec[1], rec[2], rec[3], rec[4]))
    #print(demands)
    plt.hist(demands)


# SIZE, PARKING, TOURISM, WEATHER, EVENT, DAY OF THE WEEK