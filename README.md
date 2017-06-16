# Motion detection using AWS Rekognition and Polly

This project involves motion detection along with Image Recognition, Using AWS Rekognition. 

## Requirements

### Hardware
-> Raspberry Pi 3
-> Pi Cam/ Webcam
-> 16 GB SD Card(would be sufficient)
-> Speaker

### Software/Libs
-> AWS CLI (Rekognition, Polly,S3)
-> Python(Boto3)
-> Motion Lib
-> Open CV2 

### Getting started

First, you need to create a new collection on AWS Rekognition. Creating a 'home' collection would look like:

-> python add_collection.py -n 'home'

Next, add your images to the pi-detector/faces folder. The more images of a person the better results you will get for detection. I would recommend several different poses in different lighting.

-> python add_image.py -i 'image.jpg' -c 'home' -l 'Tom'

I found the best results by taking a photo in the same area that the camera will be placed, and by using the picam. If you want to do this, I created a small python script to take a photo with a 10 second delay and then puts it into the pi-detector/faces folder. To use it:

-> python take_selfie.py 
-> python take_selfie_cam.py  (For Webcam)

Once complete, you can go back and rename the file and repeat the steps above to add your images to AWS Rekognition. Once you create a new collection, or add a new image, two reference files will be created as a future reference. These are useful if you plan on deleting images or collections in the future.

To delete a face from your collection, use the following:
-> python del_faces.py -i '000-000-000-000' -c 'home'

If you need to find the image id or a collection name, reference your faces.txt and collections.txt files.

To remove a collection:

-> python del_collections.py -c 'home'

Note that the above will also delete all the faces you have stored in AWS.

The last script is facematch.py. If you have images updated and just want to test static photos against the faces you have stored on AWS, do the following:

-> python facematch.py -i 'renji.jpg' -c 'home'

The results will be printed to screen, to include the percentage of similarity and confidence.

facematch.py is integrated along with Motion Library, once the installation is done. Only mannual thing required is to add image to collection and tag it with a name.
   
## Automated installation
  I have compiled all the neccessary commands and combined into one small script. This would install all the neccessary libs and enable the service by end of the installation. Run Install.sh from the cloned directory.
   
   

