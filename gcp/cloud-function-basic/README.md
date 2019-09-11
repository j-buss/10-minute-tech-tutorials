# Basic Cloud Function in Google Cloud Platform

With these steps we will deploy a basic cloud function that will trigger based on upload of a file to a Google Storage Bucket.

1. Create Bucket for Input
```
gsutil mb gs://YOUR_INPUT_BUCKETNAME
```
2. Within a *working directory* download the code from Google Cloud Examples:
```
curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/python-docs-samples/master/functions/gcs/main.py
```
3. Deploy the function:
```
gcloud functions deploy hello_gcs_generic --runtime python37 --trigger-resource YOUR_INPUT_BUCKET_NAME --trigger-event google.storage.object.finalize
```
4. Test the function by uploading an item to *YOUR_INPUT_BUCKETNAME*

5. Examine the cloud function logging to view the results.
