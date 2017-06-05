# Motion detection using AWS Rekognition and Polly

This project involves motion detection, along with Image Recognition. For motion detection, i have used Motion Library. 

1. The prerequisite for running this is motion library. It can be installed using below command. </br>
   sudo apt-get install motion
2. After installtion, create a hidden directory under /home/pi/ .By default the configuration will be created inside /etc/motion/
   The configuration name motion.conf </br>
   mkdir ~/.motion
3. Copy the original Motion config file to your new .motion directory.  This ensures that the original config file doesn’t get ruined        (and can be used to return Motion to it’s ‘factory settings’).</br>
   cp /etc/motion/motion.conf ~/.motion/motion.conf
   
## Automated installation
  I have compiled all the neccessary commands and combined into one small script. It would installed all the neccessary libs and enable the service by end of the installation. Run Install.sh from the cloned directory.
   
   

