# local test
`uvicorn djproject.asgi:application`

or

`gunicorn djproject.asgi:application -w 1 --threads 8 --timeout 0 -k uvicorn.workers.UvicornWorker`

# manual deploy to google cloud run
gcloud builds submit . \
--region=asia-east1 \
--config=cloudbuild.yaml \
--project=au23-grc \
--substitutions \
_SERVICE_NAME=myservice,\
_REGION=asia-east1,\
_CLOUDRUN_SERVICE_URL=https://myservice-crnvvmw3gq-de.a.run.app