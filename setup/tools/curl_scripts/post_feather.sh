#!/bin/bash
curl -X POST \
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
http://localhost:8098/ws/api/Feather/
