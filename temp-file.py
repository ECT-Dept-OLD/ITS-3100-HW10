#!/usr/bin/python3
from time import sleep
import board
import busio
from adafruit_ms8607 import MS8607
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%D %H:%M:%S")
#print("Current Time =", current_time)

i2c = busio.I2C(board.SCL, board.SDA)
sensor = MS8607(i2c)

print("%s, %.2f, %.2f, %.2f" % (current_time, sensor.pressure, sensor.temperature, sensor.relative_humidity))
