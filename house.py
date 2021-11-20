import ufirebase as firebase
from machine import Pin
import gc

class HouseRead:
    """ This class read a data from firebase (UPX4-Project) """
    def __init__(self) -> None:
        self.ledKitchen     = Pin(22, Pin.OUT)
        self.ledCoupleRoom  = Pin(23, Pin.OUT)
        self.ledLivingRoom  = Pin(25, Pin.OUT)
        self.ledBathroom    = Pin(26, Pin.OUT)
        self.ledGarage      = Pin(27, Pin.OUT)

    def houseLamps(self):
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
                self.ledKitchen.value(1)
            elif kitchen == 0:
                self.ledKitchen.value(0)

            # Couple Room
            if coupleRoom == 1:
                self.ledCoupleRoom.value(1)
            elif coupleRoom == 0:
                self.ledCoupleRoom.value(0)
            
            # Living Room
            if livingRoom == 1:
                self.ledLivingRoom.value(1)
            elif livingRoom == 0:
                self.ledLivingRoom.value(0)

            # Bathroom
            if bathroom == 1:
                self.ledBathroom.value(1)
            elif bathroom == 0:
                self.ledBathroom.value(0)

            # Garage
            if garege == 1:
                self.ledGarage.value(1)
            elif garege == 0:
                self.ledGarage.value(0)

