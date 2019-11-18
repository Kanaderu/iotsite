#!/bin/bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
        "app_id":"dayton-engineering-and-geology",
        "dev_id":"180291",
        "hardware_serial":"000DB5390864367B",
        "port":2,
        "counter":4555,
        "payload_raw":"0oCH/////w==",
        "payload_fields":{
            "b":4.2,
            "sm1":255,
            "sm2":255,
            "sm3":255,
            "sm4":255,
            "t1":28,
            "t2":35
        },
        "metadata":{
            "time":"2019-09-29T17:17:03.147714091Z",
            "frequency":904.9,
            "modulation":"LORA",
            "data_rate":"SF10BW125",
            "coding_rate":"4/5",
            "gateways":[
                {
                    "gtw_id":"rg1xx294cb6",
                    "gtw_trusted":true,
                    "timestamp":10479492,
                    "time":"",
                    "channel":5,
                    "rssi":-58,
                    "snr":9.25,
                    "rf_chain":1,
                    "latitude":39.741287,
                    "longitude":-84.18488
                }
            ]
        },
        "downlink_url":"https://integrations.thethingsnetwork.org/ttn-us-west/api/v2/down/dayton-engineering-and-geology/webhook_test?key=ttn-account-v2.kY1MRQUoGICp7C9CAEvhEdGklPVWW-ztIiU0aVRLxno"
    }' \
http://localhost:8098/ws/api/LoRaGateway/
