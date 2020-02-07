#!/bin/bash
curl -X GET \
-H "Content-Type: application/json" \
-u panda:qwerasdf \
http://127.0.0.1:9000/hooks/ | json_pp
