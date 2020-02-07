#!/bin/bash
curl -X POST \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0NzM1NDY2LCJqdGkiOiJlNWU0N2JhMzIzZmI0Y2UxOTZiY2JkNTU5OWY1N2IxZSIsInVzZXJfaWQiOjF9.Orp_ZH6eYk7NDhcyWzecvZq2qBjVkPeQ3Wa_pKfMQX4" \
-H "Content-Type: application/json" \
http://localhost:8088/ws/api/token/
