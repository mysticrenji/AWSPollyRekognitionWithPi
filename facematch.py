#!/usr/bin/env python

import boto3 as b3
import pygame, StringIO
import sys, traceback
from argparse import ArgumentParser
from time import gmtime, strftime
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
 
def get_client():
    return b3.client('rekognition')

def get_args():
    parser = ArgumentParser(description='Compare an image')
    parser.add_argument('-i', '--image')
    parser.add_argument('-c', '--collection')
    return parser.parse_args()

def check_face(client, file):
    face_detected = False
    with open(file, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()})
        if (not response['FaceDetails']):
            face_detected = False
        else: 
            face_detected = True

    return face_detected, response

def check_matches(client, file, collection):
    face_matches = False
    with open(file, 'rb') as image:
        response = client.search_faces_by_image(CollectionId=collection, Image={'Bytes': image.read()}, MaxFaces=1, FaceMatchThreshold=85)
        if (not response['FaceMatches']):
            face_matches = False
        else:
            face_matches = True

    return face_matches, response

def main():
    args = get_args()
    
    client = get_client()
    
    print '[+] Running face checks against image...'
    result, resp = check_face(client, args.image)
    import sys, traceback
      
    # Test code 
    debugging = False
    try:
		if (result):
			print '[+] Face(s) detected with %r confidence...' % (round(resp['FaceDetails'][0]['Confidence'], 2))
			print '[+] Checking for a face match...'
			resu, res = check_matches(client, args.image, args.collection)

			if (resu):
				speak="Identity matched %s with %r similarity and %r confidence..." % (res['FaceMatches'][0]['Face']['ExternalImageId'], round(res['FaceMatches'][0]['Similarity'], 1), round(res['FaceMatches'][0]['Face']['Confidence'], 2))
			        synthesizer = VoiceSynthesizer(0.9)
       				synthesizer.say(speak)
			else:
				print '[-] No face matches detected...'

		else :
			print "[-] No faces detected..."	
#       synthesizer = VoiceSynthesizer(0.1)
#       synthesizer.say("Hi Renjith.")

    except:
       print "exception occurred!"
       exc_type, exc_value, exc_traceback = sys.exc_info()
       traceback.print_exception(exc_type, exc_value, exc_traceback,
       limit=5, file=sys.stdout)

class VoiceSynthesizer(object):
    def __init__(self, volume=0.1):
       pygame.mixer.init()
       self._volume = volume
       session = Session(profile_name="default")
       self.__polly = session.client("polly")
 
    def _getVolume(self):
       return self._volume
 
    def say(self, text):
       self._synthesize(text)
 
    def _synthesize(self, text):
       # Implementation specific synthesis 
       try:
          # Request speech synthesis
          response = self.__polly.synthesize_speech(Text=text, 
                        OutputFormat="ogg_vorbis",VoiceId="Emma")
       except (BotoCoreError, ClientError) as error:
          # The service returned an error
          print(error)
          exc_type, exc_value, exc_traceback = sys.exc_info()
          traceback.print_exception(exc_type, exc_value, exc_traceback,
          limit=5, file=sys.stdout)

       # Access the audio stream from the response
       if "AudioStream" in response:
          # Note: Closing the stream is important as the service throttles on the
          # number of parallel connections. Here we are using contextlib.closing to
          # ensure the close method of the stream object will be called automatically
          # at the end of the with statement's scope.
          with closing(response["AudioStream"]) as stream:
             data = stream.read()
             filelike = StringIO.StringIO(data) # Gives you a file-like object
             sound = pygame.mixer.Sound(file=filelike)
             sound.set_volume(self._getVolume())
             sound.play() 
             while pygame.mixer.get_busy() == True:
                continue

       else:
	  # The response didn't contain audio data, exit gracefully
          print("Could not stream audio - no audio data in response")

if __name__ == '__main__':
    main()
