package service

import (
    "InfraredLeaningControlleServer/model"
)

type AirConSQL struct {}


func (AirConSQL) InsertIndoorEnv(indoorEnv *model.IndoorEnvironment) err {
    return err
}

func (AirConSQL) InsertAirConCommand(airConCommand *model.AircontrollerCommand) err {
    return err
}

func (AirConSQL) GetLatestIndoorEnv() []model.IndoorEnvironment {
    indoorEnv = model.IndoorEnvironment{}
    return indoorEnv
}

func (AirConSQL) GetLatestAirConCommand() []model.AirControllerCommand {
    command = model.AirControllerCommand{}
    return command
}
