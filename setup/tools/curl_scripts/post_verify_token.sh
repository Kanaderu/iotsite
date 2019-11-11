curl --request POST \
--header 'content-type: application/json' \
--data '{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXIxIiwiaWF0IjoxNTczMzU2NjM5LCJleHAiOjE1NzMzNTY5MzksInVzZXJfaWQiOjUsIm9yaWdfaWF0IjoxNTczMzU2NjM5fQ.6F1be26p6CRDNDFiygltrWPVgBHtsDgNembESsaP-VM"}' \
http://localhost:8088/ws/api/api-token-verify/
