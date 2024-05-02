# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(f"Average temperature: {data['temp'].mean()}")
# print(f"Maximum temperature: {data['temp'].max()}")

# print(data[data.temp == data.temp.max()])


# def celsius_to_fahrenheit(temp):
#     return (temp * 9/5) + 32
#
#
# monday = data[data.day == "Monday"]
# print(celsius_to_fahrenheit(monday["temp"]))

# create data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240501.csv")
data_dict = {"Fur Color": [], "Count": []}
for color in data["Primary Fur Color"].unique():
    if isinstance(color, str):
        data_dict["Fur Color"].append(color)
        data_dict["Count"].append(len(data[data["Primary Fur Color"] == color]))

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_fur_color_count.csv")
