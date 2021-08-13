## InfraredLeaningControlServer

### API
#### request

```
mathod  : GET
path    : /api/polling
query   : {
            "temp" : "$TEMP",
            "hum" : "$HUM",
            "press" : "$PRESS",
            "previous_command" : "T/F"
          }

response: {
            "power" : "On/Off",
            "mode" : "$MODE",
            "temp" : "$TEMP",
            "swing" : "$SWING",
            "fan" : "$FAN"
          }
```

