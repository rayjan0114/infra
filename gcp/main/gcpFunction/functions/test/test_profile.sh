#!/bin/bash
# set -x # 太吵可以關掉

if [ -z "${1}" ]; then
    echo "please provide auth token"
	exit 1
fi

echo "GET"
curl --location --request GET 'https://auth-ici2snie7q-an.a.run.app/profile?UUID=Ray' \
--header "Authorization: Bearer $1"
# curl --location --request DELETE 'https://auth-ici2snie7q-an.a.run.app/profile' \
# --header 'Content-Type: application/json' \
# --data-raw '{"UUID": "TODO666"}'

echo "DELETE"
curl --location --request DELETE 'https://auth-ici2snie7q-an.a.run.app/profile' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $1" \
--data-raw '{
    "UUID": "Ray"
}'
curl --location --request DELETE 'https://auth-ici2snie7q-an.a.run.app/profile' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $1" \
--data-raw '{
    "UUID": "Ray"
}'

echo "POST"
curl --location --request POST 'https://auth-ici2snie7q-an.a.run.app/profile' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $1" \
--data-raw '{
    "UUID": "Ray"
}'
curl --location --request POST 'https://auth-ici2snie7q-an.a.run.app/profile' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $1" \
--data-raw '{
    "UUID": "Ray"
}'


echo "PUT"
curl --location --request PUT 'https://auth-ici2snie7q-an.a.run.app/profile' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $1" \
--data-raw '{
    "UUID": "Ray",
    "Roles": ["worker"]
}' \

echo "GET"
curl --location --request GET 'https://auth-ici2snie7q-an.a.run.app/basic_info?UUID=Ray' \
--header "Authorization: Bearer $1" 
