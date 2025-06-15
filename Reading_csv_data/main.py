# with open('weather_data _Sheet.csv', 'r') as file:
#     data = file.readlines()
#     print(data)

# import csv

# with open("weather_data _Sheet.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperature_data = []
#     for row in data:
#         if row[1] != "temp":
#           temperature_data.append(int(row[1]))
#     print(temperature_data)

import pandas as pd

data = pd.read_csv("weather_data _Sheet.csv")
# print(type(data))
print(type(data["temp"]))
