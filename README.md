# AWSPollyRekognitionWithPi
Motion detection using AWS Rekognition and Polly

This project involves motion detection, along with Image Recognition. For motion detection, i have used Motion Library. 
Motion lib can be installed by below command

1. sudo apt-get install motion
2. After installtion, create a hidden directory under /home/pi/ .By default the configuration will be created inside /etc/motion/
   The configuration name motion.conf
   mkdir ~/.motion
3. Copy the original Motion config file to your new .motion directory.  This ensures that the original config file doesn’t get ruined        (and can be used to return Motion to it’s ‘factory settings’).
   cp /etc/motion/motion.conf ~/.motion/motion.conf

