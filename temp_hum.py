import sys
from flask import Flask
import Adafruit_DHT

while True:
    humidity1, temperature1 = Adafruit_DHT.read_retry(22, 27)
    humidity2, temperature2 = Adafruit_DHT.read_retry(22, 22)
    print(f'Temp 1: {temperature1} C  Humidity 1: {humidity1} %')
    print(f'Temp 2: {temperature2} C  Humidity 2: {humidity2} %')