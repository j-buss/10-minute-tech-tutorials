#!/bin/bash
# set project if one was passed
gcloud config set project

# make the commands into an array
CommandArray=(
    "gcloud compute instances create test-vm --zone=us-central1-a --machine-type=f1-micro"
    "gcloud compute instances stop test-vm"
    "gcloud compute instances start test-vm"
    "gcloud compute instances delete test-vm"
)

# Read the array values with space
for val in ""; do
  
  sleep 2m
done
