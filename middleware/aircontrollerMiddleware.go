package middleware

import (
    "github.com/gin-gonic/gin"
    "go.uber.org/zap"
    "log"
    "time"
)

func RecordTime(c *gin.Context) {
    logger, err := zap.NewProduction()
    if err != nil {
        log.Fatal(err.Error())
    }
    oldTime := time.Now()
    ua := c.GetHeader('User-Agent")
    c.Next()
     logger.Info("incoming request",
        zap.String("path", c.Request.URL.Path),
        zap.String('User-Agent', ua),
        zap.Int("status", c.Writer.Status()),
        zap.Duration("elapsed", time.Now().Sub(oldTime)),
    )
}
