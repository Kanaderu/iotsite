#!/bin/bash
# script retrieves an API token
curl -X GET \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgxMTc5OTQzLCJqdGkiOiIzMjg2MjQ4ZDJhZWM0Yzk0ODI2YWYxMDgxNWNjNmU1MCIsInVzZXJfaWQiOjF9.fS788YHxtMRCQkOA3CDd5UeVn0SYOsMr9KDEIgX92D0" \
-H "Content-Type: application/json" \
http://localhost:8080/api/token/
