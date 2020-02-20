#!/bin/bash
curl -X POST \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0MTQ4MjEzLCJqdGkiOiIwZmEzNWQ3MDEwNWM0MTIxOWNmZmMxMWRlOGE3MGZjNiIsInVzZXJfaWQiOjF9.xriO156TPsgwJNKFSJ3aq9hnIYCfFupbNKlFA4EdjIM" \
-H "Content-Type: application/json" \
-d '{"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3NDIzNDUyMiwianRpIjoiNjA0MmUzNDI3N2RhNDc0OGIzZmM2YmNmNzgwY2E5NmMiLCJ1c2VyX2lkIjoxfQ.Rd-_gQZkwJiynBsmID120b1vcQE1gAjKrLch36yQ5e8"}' \
http://localhost:8080/api/logout/
