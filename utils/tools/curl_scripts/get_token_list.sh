#!/bin/bash
curl -X GET \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0NzQ5MTUyLCJqdGkiOiJmMGIzOWNhNjQwMTY0OTIzOGZlZjE2ZGJlYTk0ODAzZCIsInVzZXJfaWQiOjF9.NBcftuxUeN0NwzZe_cKJ1wu9BEbZL8kGR1r23ypHSV0" \
-H "Content-Type: application/json" \
http://localhost:8088/ws/api/token/
