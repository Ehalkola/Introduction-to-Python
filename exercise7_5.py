import json
import urllib.request

url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)

# Create dictionaries to store data over time
region_data = {
    "Lapland": {"wind speed": 0, "count": 0},
    "Middle part of Finland": {"wind speed": 0, "count": 0},
    "Southern Finland": {"wind speed": 0, "count": 0}
}
city_data = {}

# Take data from the weather as raw data
for data in weather:
    location = data["location"]
    snow = data["snow"]
    rain = data["rain"]
    wind = data["wind"]
    area = data["area"]

    # Create conditional statement, which updates the city_data dictionary, with help of statements below
    if location not in city_data:
        city_data[location] = {"wind_speed": 0, "entries": []}
        fastest_wind = wind
        city_data[location]["wind_speed"] += fastest_wind
        city_data[location]["entries"].append({"wind": wind})

# Define each region by data from data["area"]
    if area == "lapland":
        region = "Lapland"
        region_data[region]["wind speed"] += wind
        region_data[region]["count"] += 1
    elif area == "middle":
        region = "Middle part of Finland"
        region_data[region]["wind speed"] += wind
        region_data[region]["count"] += 1
    elif area == "south":
        region = "Southern Finland"
        region_data[region]["wind speed"] += wind
        region_data[region]["count"] += 1

# Print the average wind speed for each region
for region, data in region_data.items():
    if data["count"] > 0:
        average_wind_speed = round(data["wind speed"] / data["count"], 1)
        print(f"Average wind speed in {region}: {average_wind_speed} m/s")
    else:
        print(f"{region}: No data available")

# Find a cities with the weakest, fastest wind speeds
strongest_city = max(city_data, key=lambda city: city_data[city]["wind_speed"])
print("\n" f"Strongest wind today at location: {strongest_city} {city_data[strongest_city]['wind_speed']} m/s")
weakest_city = min(city_data, key=lambda city: city_data[city]["wind_speed"])
print(f"Weakest wind today at location: {weakest_city} {city_data[weakest_city]['wind_speed']} m/s")
