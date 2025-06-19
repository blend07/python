import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("weather_tokyo_data.csv")

#1

all_values_string = df["temperature"].iloc[0]

cleaned_string = all_values_string.replace("(", "").replace(")", "")

values = cleaned_string.split()

float_values = [float(v) for v in values]

average = sum(float_values) / len(float_values)

print(f"Average Temperature: {average:.2f}")


#2

df.columns = df.columns.str.strip()

df["date"] = pd.to_datetime(df["year"].astype(str) + "/" + df["day"], format="%Y/%m/%d")

df["temperature"] = pd.to_numeric(df["temperature"], errors='coerce')

df["month"] = df["date"].dt.month

monthly_avg = df.groupby("month")["temperature"].mean()

plt.figure(figsize=(10, 6))
monthly_avg.plot(kind="bar", color="skyblue")
plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


#3
hottest_day = df.loc[df["temperature"].idxmax()]
coldest_day = df.loc[df["temperature"].idxmin()]

print("\nHottest Day:")
print(hottest_day)

print("\nColdest Day:")
print(coldest_day)

plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["temperature"], marker='o', linestyle='-', color='orange')
plt.title("Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Average Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()


#4a
plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["temperature"], marker='o', linestyle='-', color='orange')
plt.title("Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()

#4b
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Fall"

df["season"] = df["month"].apply(get_season)

seasonal_avg = df.groupby("season")["temperature"].mean().reindex(["Winter", "Spring", "Summer", "Fall"])

plt.figure(figsize=(8, 5))
seasonal_avg.plot(marker='o', color='green', linestyle='-')
plt.title("Seasonal Average Temperature")
plt.xlabel("Season")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()