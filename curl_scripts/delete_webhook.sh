#!/bin/bash
curl -X DELETE \
-H "Content-Type: application/json" \
-u panda:qwerasdf \
http://127.0.0.1:9000/hooks/64963acd-d8ed-4e83-bc4e-543d30fdbf82/ | json_pp
