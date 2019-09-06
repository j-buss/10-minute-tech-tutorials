#!/bin/bash
for i in {1..5}
do
   curl -s https://temp-project-002.appspot.com > /dev/null
   sleep 5
done
