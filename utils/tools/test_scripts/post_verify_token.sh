#!/bin/bash
# check the return status of the reply {200 is verified and valid}
curl -X POST \
-H 'content-type: application/json' \
-d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoic2xpZGluZyIsImV4cCI6MTYxMjcxNTc3NCwianRpIjoiYzcwYjcwYzZiYjZiNDA4ZThhYmZkNzc4NDEwNDQ5YmMiLCJyZWZyZXNoX2V4cCI6MTY0NDI1MTc3NCwidXNlcl9pZCI6MX0.-fWnaubXVhQtnSEn9BQ72aVIiNhlaQYzCdCKP71q4Qo"}' \
http://localhost:8080/api/verify/
