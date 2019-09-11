# Basic Cloud Function in Google Cloud Platform

1. Create Bucket for Input
`gsutil mb gs://YOUR_INPUT_BUCKETNAME`
1. Within a *working directory* download the code from Google Cloud Examples:
`curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/python-docs-samples/master/functions/gcs/main.py `
1. Deploy the function:
```
gcloud functions deploy hello_gcs_generic --runtime python37 --trigger-resource YOUR_INPUT_BUCKET_NAME --trigger-event google.storage.object.finalize
```
