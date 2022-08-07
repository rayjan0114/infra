#!/bin/bash

echo "GET"
curl --location --request GET 'localhost:5555/profile?UUID=Ray'
# curl --location --request DELETE 'localhost:5555/profile' \
# --header 'Content-Type: application/json' \
# --data-raw '{"UUID": "TODO666"}'

echo "DELETE"
curl --location --request DELETE 'localhost:5555/profile' \
--header 'Content-Type: application/json' \
--data-raw '{
    "UUID": "Ray"
}'
curl --location --request DELETE 'localhost:5555/profile' \
--header 'Content-Type: application/json' \
--data-raw '{
    "UUID": "Ray"
}'

echo "POST"
curl --location --request POST 'localhost:5555/profile' \
--header 'Content-Type: application/json' \
--data-raw '{
    "UUID": "Ray"
}'
curl --location --request POST 'localhost:5555/profile' \
--header 'Content-Type: application/json' \
--data-raw '{
    "UUID": "Ray"
}'


echo "PUT"
curl --location --request PUT 'localhost:5555/profile' \
--header 'Content-Type: application/json' \
--data-raw '{
    "UUID": "Ray",
    "Role": "worker"
}' \

echo "GET"
curl --location --request GET 'localhost:5555/profile?UUID=Ray'
