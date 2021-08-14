package service

import (
    "github.com/go-xorm/xorm"
    "errors"
    "log"
    "InfraredLeaningControleServer/model"
)

var DbEngine *xorm.Engine

func init() {
    driverName := "mysql"
    DsName := "**********"
    err := errors.New("")
    DbEngine, err = xorm.NewEngine(driverName, DsName)
    if err != nil && err.Error() != ""{
        log.Fatal(err.Error())
    }
    DbEngine.ShowSQL(true)
    DbEngine.SetMaxOpenConns(2)
    DbEngine.Sync2(new(model.AirController))
}
