#!/bin/bash
curl -X POST \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoic2xpZGluZyIsImV4cCI6MTYwNjI5MDA2OSwianRpIjoiN2U0ZjE5NDI5NDIzNGE4ZTkxOGEzNTFmMmJkYTg0NWUiLCJyZWZyZXNoX2V4cCI6MTYzNzgyNjA2OSwidXNlcl9pZCI6MX0.WV_DHYa_M9XyO2ThUF10ZcVLr5i6p0ODj5Erv8IO1-A" \
-H "Content-Type: application/json" \
-d '{
        "dev_id": 1,
        "metadata": {
              "location": "Apartment",
              "latitude": 39.77710000,
              "longitude": -83.99720000,
              "time": "2019-10-02T19:17:10.067889-04:00"
        },
        "data": [
         {
             "sensor_id": 1,
             "sensor_type": "Temperature",
             "sensor_data": 19.813,
             "sensor_units": "C"
         },
         {
             "sensor_id": 2,
             "sensor_type": "Temperature",
             "sensor_data": 16.188,
             "sensor_units": "C"
         }
         ]
    }' \
http://localhost:8088/ws/api/Feather/
