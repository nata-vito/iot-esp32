import network

class connect:
    def __init__(self, ssid, password) -> None:
        self.ssid       = ssid
        self.password   = password
        self.sta_if     = network.WLAN(network.STA_IF)                                # Instance to station, please read the documentation for more details
    
    def wifi(self):
        if(self.sta_if.isconnected() == False):
            self.sta_if.active(True)                                               # Activating the station mode 
            self.sta_if.connect(self.ssid, self.password)                                    # Conect to your wifi router

            while self.sta_if.isconnected() == False:
                pass
    
    def verify(self):
        if(self.sta_if.sta_if.isconnected()):
            print("Connected")
            print(self.sta_if.ifconfig())
        else:
            print("Not Connected")
    
    def print(self):
        info = "ssid: " + self.ssid + "\n" + "password: " + self.password + "\n"
        return info
