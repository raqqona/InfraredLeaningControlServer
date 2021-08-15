package model

type AirController struct {
    Power byte
    Mode byte
    Temp byte
    Swing byte
    Fan byte
    LastCommand bool
}

type IndoorEnvironment struct {
    Temp float64
    Hum float64
    Press float64
}
