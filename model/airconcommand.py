import json

class AirConCommnad():
    def __init__(self, command):
        self.power = command['power']
        self.mode = command['mode']
        self.temp = command['temp']
        self.swing = command['swing']
        self.fan = command['fan']

