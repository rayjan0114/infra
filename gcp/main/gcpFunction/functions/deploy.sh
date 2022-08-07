#!/bin/bash

if [ -z "${1}" ]; then
    echo "please provide your function name"
    echo "ex: ./deploy.sh <func_name>"
    echo "maybe: `cat *.py | grep def`"
	exit 1
fi

echo "your function name: $1"
# cd ..
# rm -rf deploy
# cp -r gcf deploy
# cd deploy
# mv "$1.py" main.py

gcloud beta functions deploy $1 \
    --runtime python37 \
    --trigger-http \
    --region=asia-northeast1 \
    --max-instances=5 \
    --ignore-file=.gcloudignore \
    --security-level=secure-always \
    --quiet

gcloud functions add-iam-policy-binding $1 \
   --region asia-northeast1 \
   --member "serviceAccount:99892723132-compute@developer.gserviceaccount.com" \
   --role "roles/cloudfunctions.invoker" \
   --project sideproject-306713
# cd ../gcf
