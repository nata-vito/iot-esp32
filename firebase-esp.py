import ufirebase as firebase
import network 
from machine import Pin
import gc

gc.collect()
ssid = 'VITORINO 2.4 G'
password = '33435337'
sta_if = network.WLAN(network.STA_IF)                                # Instance to station, please read the documentation for more details

if(sta_if.isconnected() == False):
    sta_if.active(True)                                               # Activating the station mode 
    sta_if.connect(ssid, password)                                    # Conect to your wifi router

    while sta_if.isconnected() == False:
        pass

print("Connected")
print(sta_if.ifconfig())

led = Pin(22, Pin.OUT)

while True:
    ledApi = firebase.get("https://iot-esp32-8b0e5-default-rtdb.firebaseio.com/IoT/led")
    print(ledApi)
    if ledApi == '1':
        print("LED ON")
        led.value(1)
    elif ledApi == '0':
        print("LED OFF")
        led.value(0)