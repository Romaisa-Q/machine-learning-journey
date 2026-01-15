import pandas as pd

weather = pd.read_csv("weather.csv")

print("Weather Data:\n")
print(weather)

avg_temp = weather["temperature"].mean()
max_temp = weather["temperature"].max()
min_temp = weather["temperature"].min()

print("\nAverage Temperature:", avg_temp)
print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)

hottest_day = weather.loc[weather["temperature"].idxmax()]
print("\nHottest Day Details:")
print(hottest_day)
coldest_day = weather.loc[weather["temperature"].idxmin()]
print("\nColdest Day Details:")
print(coldest_day)
print("\nHumidity Data:\n")
print(weather[["day", "humidity"]])

