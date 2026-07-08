import serial
import csv
import time
from datetime import datetime

# -----------------------------
# Configuration
# -----------------------------
PORT = "/dev/cu.usbserial-1420"      # Change if your Arduino port changes
BAUD_RATE = 9600
OUTPUT_FILE = "environment_data.csv"

print("======================================")
print(" Environmental Dashboard Logger")
print("======================================")
print("Sampling interval : 5 seconds")
print(f"Serial Port       : {PORT}")
print("Press Ctrl+C to stop.\n")

# -----------------------------
# Connect to Arduino
# -----------------------------
arduino = serial.Serial(PORT, BAUD_RATE)
time.sleep(2)   # Allow Arduino to reset after opening serial port

# -----------------------------
# Create CSV file
# -----------------------------
file = open(OUTPUT_FILE, "w", newline="")
writer = csv.writer(file)

writer.writerow(["Sample", "Timestamp", "Temperature (°C)", "Humidity (%)"])

sample = 1

print("Logging started...\n")

try:
    while True:

        # Read one line from Arduino
        line = arduino.readline().decode("utf-8").strip()

        # Expected format:
        # 27.5,61.0
        data = line.split(",")

        if len(data) == 2:

            try:
                temperature = float(data[0])
                humidity = float(data[1])

            except ValueError:
                # Skip corrupted readings
                continue

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            writer.writerow([
                sample,
                timestamp,
                temperature,
                humidity
            ])

            # Save every reading immediately
            file.flush()

            print(
                f"Sample {sample:05d} | "
                f"{timestamp} | "
                f"Temp: {temperature:.1f} °C | "
                f"Humidity: {humidity:.1f}%"
            )

            sample += 1

except KeyboardInterrupt:
    print("\nLogging stopped by user.")

finally:
    file.close()
    arduino.close()
    print(f"\nData saved to '{OUTPUT_FILE}'.")
    print("Serial connection closed.")