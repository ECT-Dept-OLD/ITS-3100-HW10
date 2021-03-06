#!/usr/bin/python3
from time import sleep
import board
import busio
from adafruit_ms8607 import MS8607

i2c = busio.I2C(board.SCL, board.SDA)
sensor = MS8607(i2c)

print("Pressure: %.2f hPa" % sensor.pressure)
print("Temperature: %.2f C" % sensor.temperature)
print("Humidity: %.2f %% rH" % sensor.relative_humidity)
