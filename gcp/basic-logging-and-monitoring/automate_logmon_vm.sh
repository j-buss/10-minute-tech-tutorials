#!/bin/bash
# set project if one was passed
#gcloud config set project
echo Script name: $0
echo $# arguments

if [ $# -ne 3 ]; then
        echo "illegal number of parameters"
        echo "Argument: vm_name project_id zone"
else
    vm_name=$1
    project_id=$2
    zone=$3

    # make the commands into an array
    declare -a CommandArray=(
        "gcloud compute instances create test-vm --zone=us-central1-a --machine-type=f1-micro"
        "gcloud compute instances stop test-vm"
        "gcloud compute instances start test-vm"
        "gcloud compute instances delete test-vm"
    )

    # Read the array values with space
    for val in "${CommandArray[@]}"; do
        echo $val 
        sleep 2m
    done
fi
