import json

class IndoorEnv():
    def __init__(self):
        self.temp = 0
        self.hum = 0
        self.press = 0

    def set_data_from_json(self, json):
        self.temp = json['temp']
        self.hum = josn['hum']
        self.press = json['press']

    def set_data_from_sql(self, sql):
        self.temp = sql[0]
        self.hum = sql[1]
        self.press = sql[2]

