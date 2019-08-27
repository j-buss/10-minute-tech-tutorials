#!/bin/bash
echo ------------------
echo Script name: $0
echo ------------------
echo Tutorial script to cycle through: creation, stop, start, delete of a compute engine vm
echo    with the intent of examining logging in Stackdriver as a result of those actions
echo ------------------
echo $# arguments

if [ $# -ne 3 ]; then
        echo "illegal number of parameters"
        echo "Argument: vm_name project_id zone"
else
    vm_name=$1
    project_id=$2
    zone=$3

	# Set GCP Project Id
	gcloud config set project $project_id

    # Make the commands into an array
    declare -a CommandArray=(
        "gcloud compute instances create $vm_name --zone=$zone --machine-type=f1-micro"
        "gcloud compute instances stop --quiet --zone=$zone $vm_name"
        "gcloud compute instances start --quiet --zone=$zone $vm_name"
        "gcloud compute instances delete --quiet --zone=$zone $vm_name"
    )

    # Read the array values with space
    for val in "${CommandArray[@]}"; do
        echo $val 
		$val
        sleep 5s
    done
fi
