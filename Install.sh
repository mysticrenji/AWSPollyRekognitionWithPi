#!/bin/bash

# Install script for Greeting using Polly
# Renjith Ravindranathan
# 30/05/2017

echo '[+] Updating and installing dependencies...'
sudo apt-get update && apt-get -y upgrade

echo '[+] Freeing up space. Removing Wolfram-Engine...'
sudo apt-get purge wolfram-engine

sudo apt-get install -y build-essential python-setuptools awscli motion

pip install boto3 watchdog simplejson
rm -rf ~/.cache/pip

echo '[+] Configuring AWS...'
aws configure

cd

echo '[+] Cloning from the repo...'

git clone https://github.com/mysticrenji/AWSPollyRekognitionWithPi.git


echo '[+] Configuring Motion Library...'

sudo mkdir ~/.motion

cd ~/AWSPollyRekognitionWithPi

echo '[+] Copying Motion Configuration to root and home directory'

sudo cp ./config/motion.conf  /etc/motion/

sudo cp ./config/motion.conf  ~/.motion/

echo '[+] Creating service for AWS Polly Rekognition for auto start'

sudo cp ./services/aws-polly-greeting.service /etc/systemd/system/

sudo cp ./services/aws-polly-greeting.sh /usr/local/bin/

sudo chmod 744 /usr/local/bin/aws-polly-greeting.sh

sudo chmod 664 /etc/systemd/system/aws-polly-greeting.service

echo '[+] Reloading Services'

sudo systemctl daemon-reload

echo '[+] Enabling AWS Polly Rekognition service'

sudo systemctl enable aws-polly-greeting.service

echo '[+] Done!'

exit 0

