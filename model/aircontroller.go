package model

type AirController struct {
    Power byte 'json:"power"'
    Mode byte 'json:"mode"'
    Temp byte 'json:"temp"'
    Swing byte 'json:"swing"'
    Fan byte 'json:"fan"'
    NextCommand bool
}

type IndoorEnvironment struct {
    Temp float64 'json:"temp"'
    Hum float64 'json:"hum"'
    Press float64 'json:"press"'
    LastCommand bool 'json:"command"'
}
