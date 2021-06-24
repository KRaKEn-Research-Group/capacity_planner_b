import pandas
from pandas.tseries.offsets import Day

weather = pandas.read_csv("data/out/network_data_weather_quali.csv")
demand = pandas.read_csv("data/out/network_data4.csv")
month = demand["MONTH"]
day = demand["DAY"]
weekday = demand["WEEKDAY"]
cars = demand["CARS"]
weather = weather.join(month)
weather = weather.join(weekday)
weather = weather.join(day)
weather = weather.join(cars)

pandas.DataFrame(weather).to_csv("data/out/network_data_glued2.csv")
