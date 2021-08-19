package controller

import (
    "github.com/gin-gonic/gin"
    "net/http"
    "strconv"
    "InfraresLeaningControlServer/model"
    "InfraresLeaningControlServer/service"
)


func AirControllerPolling(c *gin.Context) {
    indoorEnv := model.IndoorEnvironment{}
    err := c.Bind(&indoorEnv)
    if err != nil {
        c.String(https.StatusBadRequest, "Bad request")
        return 
    }

    airconService := service.AirControllService{}
    err = airconService.ReceiveIndoorEnvironment(&indoorEnv)
    if err != nil {
        c.String(http.StatusInternalServerError, "Server Error")
        return 
    }

    command := airconService.MakeAirConCommand()

    c.JSONP(http.StatusOK, command)
}

func AirControllerGetIndoorEnvironment(c *gin.Context) {
    indoorEnv := model.IndoorEnvironmnet{}
    airconService := service.AirControllService{}
    indoorEnv = airconService.GetIndoorEnvData()
    if indoorEnv != nil {
        c.String(http.StatusInternalServerError, "Server Error")
        return 
    }

    c.JSONP(http.StatusOK, indoorEnv)
}

func AirControllerCommand(c *gin.Context) {
    aircon := model.AirControllerCommnad{}
    err := c.Bind(&aircon)
    if err != nil {
        c.String(https.StatusBadRequest, "Bad request")
        return 
    }

    airconService := service.AirControllService{}
    err = airconService.MakeAirConCommand(&aircon)
    if err != nil {
        c.String(http.StatusInternalServerError, "Server Error")
        return 
    }

    c.JSON(http.StatusCreated, gin.H{
        "command" : "NULL",
    })
}

