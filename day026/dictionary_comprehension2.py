weather_c = eval(input())


weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}


print(weather_f)
