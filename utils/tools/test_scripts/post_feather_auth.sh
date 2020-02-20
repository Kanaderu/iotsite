#!/bin/bash
# post some example feather data with a valid API token
curl -X POST \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoic2xpZGluZyIsImV4cCI6MTYxMjcxNTc3NCwianRpIjoiYzcwYjcwYzZiYjZiNDA4ZThhYmZkNzc4NDEwNDQ5YmMiLCJyZWZyZXNoX2V4cCI6MTY0NDI1MTc3NCwidXNlcl9pZCI6MX0.-fWnaubXVhQtnSEn9BQ72aVIiNhlaQYzCdCKP71q4Qo" \
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
http://localhost:8080/api/Feather/
