# # with open('weather_data _Sheet.csv', 'r') as file:
# #     data = file.readlines()
# #     print(data)

# # import csv

# # with open("weather_data _Sheet.csv", "r") as data_file:
# #     data = csv.reader(data_file)
# #     temperature_data = []
# #     for row in data:
# #         if row[1] != "temp":
# #           temperature_data.append(int(row[1]))
# #     print(temperature_data)

# import pandas as pd

# data = pd.read_csv("weather_data _Sheet.csv")
# # print(type(data))
# # print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# print(data["temp"].mean())  # Calculate the mean temperature
# print(data["temp"].max())   # Find the maximum temperature
# print(data["condition"])  # Access the 'condition' column
# print(data.condition)  # Access the 'condition' column using dot notation
# print(data[data.day == "Monday"])  # Filter data for Monday

# monday = data[data.day == "Monday"]
# monday_temp_F = monday["temp"].values[0] * 9/5 + 32  # Convert Monday's temperature to Fahrenheit
# print(monday_temp_F)  # Print Monday's temperature in Fahrenheit

#create a data frame from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv", index=False)  #  create and Save the DataFrame to a CSV file without the index

import pandas as pd
# Read the CSV file containing squirrel census data
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250615.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])  # Create a boolean
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])  # Create a boolean series for red squirrels
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])  # Create a boolean series for black squirrels

# Create a boolean series for gray squirrels
print(gray_squirrel_count)  # Print the count of gray squirrels
print(red_squirrel_count)  # Print the count of red squirrels
print(black_squirrel_count)  # Print the count of black squirrels

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}
df = pd.DataFrame(data_dict)  # Create a DataFrame from the dictionary
df.to_csv("squirrel_count.csv", index=False)  # Save the DataFrame to a CSV file without the index