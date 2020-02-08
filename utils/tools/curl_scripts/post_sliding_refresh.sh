#!/bin/bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3NDgyMTcxMiwianRpIjoiYTFlNGU1ZTUwZjI3NGEyZDg1MjM1ODNkODc5NTU2OWMiLCJ1c2VyX2lkIjoxfQ.4DesH_sqavUMulP7Lmg8m1wwZpGE1SVi0sJj-7KkihM"}' \
http://localhost:8080/api/refresh-token/
