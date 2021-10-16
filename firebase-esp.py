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

ledKitchen        = Pin(22, Pin.OUT)
ledCoupleRoom     = Pin(23, Pin.OUT)
ledLivingRoom     = Pin(25, Pin.OUT)
ledBathroom       = Pin(26, Pin.OUT)
ledGarage         = Pin(27, Pin.OUT)

def houseLamps():

    kitchen         = firebase.get("https://proud-limiter-323718-default-rtdb.firebaseio.com/kitchen/lamp")
    coupleRoom      = firebase.get("https://proud-limiter-323718-default-rtdb.firebaseio.com/coupleRoom/lamp")
    livingRoom      = firebase.get("https://proud-limiter-323718-default-rtdb.firebaseio.com/livingRoom/lamp")
    bathroom        = firebase.get("https://proud-limiter-323718-default-rtdb.firebaseio.com/bathRoom/lamp")
    garege          = firebase.get("https://proud-limiter-323718-default-rtdb.firebaseio.com/garage/lamp")

    # Kitchen
    if kitchen == 1:
        ledKitchen.value(1)
    elif kitchen == 0:
        ledKitchen.value(0)

    # Couple Room
    if coupleRoom == 1:
        ledCoupleRoom.value(1)
    elif coupleRoom == 0:
        ledCoupleRoom.value(0)
    
    # Living Room
    if livingRoom == 1:
        ledLivingRoom.value(1)
    elif livingRoom == 0:
        ledLivingRoom.value(0)

    # Bathroom
    if bathroom == 1:
        ledBathroom.value(1)
    elif bathroom == 0:
        ledBathroom.value(0)

    # Garage
    if garege == 1:
        ledGarage.value(1)
    elif garege == 0:
        ledGarage.value(0)


while True:
    houseLamps()