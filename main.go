package main

import (
    "github.com/gin-gonic/gin"
    _ "github.com/go-sql-driver/mysql"
    "InfraredLeaningControlServer/controller"
    "InfraredLeaningControlServer/middleware"
)

func main() {
    engine := gin.Default()
    engine.Use(middleware.RecordTime)

    aircontrollerEngine := engine.Group("/InfraredLeaningControleServer") {
        api := aircontrollerEngine.Group("/api") {
            api.GET("/polling", controller.AirControllerPolling)
            api.GET("/getIndoorEnv", controller.AirControllerGetStatus)
            api.POST("/command", controller.AirContollerCommand)
        }
    }
    engine.Run(":8080")
}
