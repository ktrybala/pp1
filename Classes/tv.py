class TV:
    
    """Creating TV object and defining its atributes"""

    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        
    def show_status(self):
        if self.is_on == False:
            print("TV is off")
        elif self.is_on:
            print(f"TV is on, channel {self.channel_no}")
    
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def change_channel(self):
        self.channel_no = int(input("Set channel: "))
    
    def set_channels(self,channels):
        self.channels = channels
        
    def show_channels(self):
        x = 1
        for i in self.channels:
            print(f"{x}. {i}")
            x += 1
    

tv1 = TV()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.change_channel()
tv1.show_status()
tv1.turn_off()
tv1.show_status()
tv1.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
tv1.show_channels()
    