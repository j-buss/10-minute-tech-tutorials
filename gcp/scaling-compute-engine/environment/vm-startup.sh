#! /bin/bash
apt-get update
apt-get install -y git
git clone https://github.com/j-buss/learn-to-scale-google-compute
cd learn-to-scale-google-compute
python3 -m http.server 8080
