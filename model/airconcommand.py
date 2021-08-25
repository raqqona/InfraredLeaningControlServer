import json

class AirConCommnad():
    def __init__(self):
        self.power = 0
        self.mode = 0
        self.temp = 0
        self.swing = 0
        self.fan = 0

    def set_data_from_json(self, command):
        self.power = json['power']
        self.mode = json['mode']
        self.temp = json['temp']
        self.swing = json['swing']
        self.fan = json['fan']
    
    def set_data_from_sql(self, sql):
        self.power = sql[0]
        self.mode = sql[1]
        self.temp = sql[2]
        self.swing = sql[3]
        self.fan = sql[4]
