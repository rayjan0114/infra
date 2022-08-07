- Deploying the Endpoints configuration

    gcloud endpoints services deploy openapi-functions.yaml \
    --project sideproject-306713

- To build the service config into a new ESPv2 docker image:

    ./gcloud_build_image -s auth-ici2snie7q-de.a.run.app \
        -c 2021-05-24r2 -p sideproject-306713

- Deploying the ESPv2 container

    gcloud run deploy auth \
    --image="gcr.io/sideproject-306713/endpoints-runtime-serverless:2.26.1-auth-ici2snie7q-de.a.run.app-2021-05-24r2" \
    --allow-unauthenticated \
    --platform managed \
    --project=sideproject-306713 \
    --region=asia-northeast1
