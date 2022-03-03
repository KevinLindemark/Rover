try:
  import usocket as socket
except:
  import socket

from machine import Pin, PWM
import network

import esp
esp.osdebug(None)

import gc
gc.collect()
# wifi hotspot credentials for Rover to connect to
ssid = 'ESP32'
password = '12345678'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())


