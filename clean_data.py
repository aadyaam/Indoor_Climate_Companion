import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read the CSV
df = pd.read_csv("environment_data.csv")
df["Timestamp"]=pd.to_datetime(df["Timestamp"])

print("First 5 rows:")
print(df.head())

print("\n----------------------------")

print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))

print("\n----------------------------")

print("Data Types:")
print(df.dtypes)

print("\n----------------------------")

print("Missing Values:")
print(df.isnull().sum())

print("\n----------------------------")

print("Statistics:")
print(df.describe())

start_time=df["Timestamp"].min()
end_time=df["Timestamp"].max()

print("\nExperiment Started:")
print(start_time)
print("\nExperiment Ended:")
print(end_time)

duration=end_time-start_time

print("\nExperiment Duration:")
print(duration)

plt.figure(figsize=(12,5))

plt.plot(
    df["Timestamp"],
    df["Temperature (°C)"],
    linewidth=2,
    marker=".",
    markersize=3
)

plt.title("Temperature vs Time [07-07-2026]")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")

plt.grid(True)

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("temprature_vs_time.png", dpi=300)
plt.show()

plt.figure(figsize=(12,5))

plt.plot(
    df["Timestamp"],
    df["Humidity (%)"],
    linewidth=2,
    marker=".",
    markersize=3
)

plt.title("Humidity vs Time [07-07-2026]")
plt.xlabel("Time")
plt.ylabel("Hymidity (°C)")

plt.grid(True)

plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("humidity_vs_time.png", dpi=300)
plt.show() 

plt.figure(figsize=(8,6))

plt.scatter(
    df["Temperature (°C)"],
    df["Humidity (%)"]
)

plt.title("Temperature vs Humidity[07-07-2026]")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")

plt.grid(True)
plt.tight_layout()
plt.savefig("temprature_vs_humidity.png", dpi=300)
plt.show()