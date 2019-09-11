Leverage a simple test function.

Create the Input Bucket:
gsutil mb gs://YOUR_INPUT_BUCKETNAME

Deploy the function:
gcloud functions deploy hello_gcs_generic --runtime python37 --trigger-resource \ 
    YOUR_INPUT_BUCKET_NAME --trigger-event google.storage.object.finalize
