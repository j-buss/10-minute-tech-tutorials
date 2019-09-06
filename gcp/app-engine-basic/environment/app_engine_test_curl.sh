#!/bin/bash
echo ------------------
echo Script name: $0
echo ------------------
echo Tutorial script to cycle through curl commands to put some load on an app-engine app
echo ------------------
echo $# arguments
if [ $# -lt 3 ]; then
    echo "illegal number of parameters"
    echo "Argument: project_id number_of_loops curl_delay_seconds route-optional"
else
    project_id=$1
    number_of_loops=$2
    curl_delay_seconds=$3
	route=${4:-}
    for ((i=1;i<=number_of_loops;i++)); do
        curl -s https://$project_id.appspot.com/$route > /dev/null
        sleep $curl_delay_seconds
    done
fi
