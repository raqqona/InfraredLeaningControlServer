package service

import (
    "InfraredLeaningControlleServer/model"
)

type AirControllerService struct {}


func (AirControllerService) ReceiveIndoorEnvironmentData(indoorEnv *model.IndoorEnvironment) err {
    _, err := DbEngine.Insert(indoorEnv)
    if err != nil {
        return err
    }
    return nil
}

func (AirControllerService) GetIndoorEnvironmentData() []model.IndoorEnvironment {
    indoorEnv := make([]model.IndoorEnvironment, 0)
    err := DbEngine.Distinct("Temp", "Hum", "Press").Limit(10.0).Find(&indoorEnv)
    if err != nil {
        panic(err)
    }
    return indoorEnv
}

func (AirControllerService) MakeAirConComannd() []model.AirControllerCommand {
    aircon := make([]model.AirControllerCommand, 0)
    err := DbEngine.Distinct("Power", "Mode", "Temp", "Swing", "Fan", "LastCommand").Limit(10.0).Find(&aircon)
    if err != nil {
        panic(err)
    }
    return aircon
}

func (AirControllerService) ReceiveAirConCommand(aircon *model.IndoorEnvironment) err {
    _, err := DbEngine.Insert(aircon)
    if err != nil {
        return err
    }
    return nil
}
