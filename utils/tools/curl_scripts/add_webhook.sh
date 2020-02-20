#!/bin/bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"event": "sensor_data.*", "url": "https://webhook.site/d574359c-0211-49db-8bb1-f9b9df0a051e"}' \
-u panda:qwerasdf http://127.0.0.1:9000/hooks/ | json_pp
