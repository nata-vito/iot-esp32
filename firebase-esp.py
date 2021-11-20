import _thread
import gc
import conection

gc.collect()

# Wifi SetUp
connect = conection.connect
connect.__init__(connect, 'VITORINO 2.4 G', '33435337')
print(connect.print(connect))
print(connect.verify(connect))

""" ssid = 'VITORINO 2.4 G'
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
    while(True):
        kitchen         = firebase.get("https://proud-limiter-323718-default-rtdb.firebaseio.com/luzes/cozinha/state")
        coupleRoom      = firebase.get("https://proud-limiter-323718-default-rtdb.firebaseio.com/luzes/quarto/state")
        livingRoom      = firebase.get("https://proud-limiter-323718-default-rtdb.firebaseio.com/luzes/sala/state")
        bathroom        = firebase.get("https://proud-limiter-323718-default-rtdb.firebaseio.com/luzes/banheiro/state")
        garege          = firebase.get("https://proud-limiter-323718-default-rtdb.firebaseio.com/luzes/garagem/state")

        print("Cozinha: ", kitchen)
        print("Quarto: ", coupleRoom)
        print("Sala: ", livingRoom)
        print("Banheiro: ", bathroom)
        print("Garagem: ", garege) 
        print("\n")

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

try:
    _thread.start_new_thread(houseLamps, ())
except:
    print("Error: unable to start thread") """