#!/bin/bash
# Post user logout to inform to invalidate tokens
# TODO: testing
curl -X POST \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoic2xpZGluZyIsImV4cCI6MTYxMjcxNTc3NCwianRpIjoiYzcwYjcwYzZiYjZiNDA4ZThhYmZkNzc4NDEwNDQ5YmMiLCJyZWZyZXNoX2V4cCI6MTY0NDI1MTc3NCwidXNlcl9pZCI6MX0.-fWnaubXVhQtnSEn9BQ72aVIiNhlaQYzCdCKP71q4Qo" \
-H "Content-Type: application/json" \
-d '{"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3NDIzNDUyMiwianRpIjoiNjA0MmUzNDI3N2RhNDc0OGIzZmM2YmNmNzgwY2E5NmMiLCJ1c2VyX2lkIjoxfQ.Rd-_gQZkwJiynBsmID120b1vcQE1gAjKrLch36yQ5e8"}' \
http://localhost:8080/api/logout/
