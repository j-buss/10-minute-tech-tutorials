# Basic Cloud Function in Google Cloud Platform

1. Create Bucket for Input
`gsutil mb gs://YOUR_INPUT_BUCKETNAME`
2. Deploy the function:
```gcloud functions deploy hello_gcs_generic --runtime python37 --trigger-resource YOUR_INPUT_BUCKET_NAME --trigger-event google.storage.object.finalize```
