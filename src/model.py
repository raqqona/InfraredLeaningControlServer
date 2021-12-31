import json

class AirConCommnad():
    def __init__(self):
        self.power = 0
        self.mode = 0
        self.temp = 0
        self.swing = 0
        self.fan = 0
        self.latest_command = False

    def set_data_from_json(self, json):
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

    def export_json(self, flag):
        self.latest_command = flag
        json_dict = {}
        json_dict['power'] = self.power
        json_dict['mode'] = self.mode
        json_dict['temp'] = self.temp
        json_dict['swing'] = self.swing
        json_dict['fan'] = self.fan
        json_dict['latest_command'] = self.latest_command

        return json.dumps(json_dict)

class IndoorEnv():
    def __init__(self):
        self.temp = 0
        self.hum = 0
        self.press = 0

    def set_data_from_json(self, json):
        self.temp = json['temp']
        self.hum = json['hum']
        self.press = json['press']

    def set_data_from_sql(self, sql):
        self.temp = sql[0]
        self.hum = sql[1]
        self.press = sql[2]

    def export_json(self):
        json_dict = {}
        json_dict['power'] = self.power
        json_dict['hum'] = self.hum
        json_dict['press'] = self.press

        return json.dumps(json_dict)
