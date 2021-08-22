package model

type AirControllerCommnad struct {
    Power byte 'json:"field_byte"'
    Mode byte 'json:"field_byte"'
    Temp byte 'json:"field_byte"'
    Swing byte 'json:"field_byte"'
    Fan byte 'json:"field_byte"'
    LastCommand bool 'json:"field_bool"'
}

type IndoorEnvironment struct {
    Temp float64 'json:"temp"'
    Hum float64 'json:"hum"'
    Press float64 'json:"press"'
    LastCommand bool 'json:"command"'
}
