#! /usr/bin/env python
import pygame, StringIO
import sys, traceback
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing

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
                        OutputFormat="ogg_vorbis",VoiceId="Joanna")
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

if __name__ == "__main__":
    import sys, traceback
    # Test code 
    debugging = False
    try: 
       synthesizer = VoiceSynthesizer(0.9)
       synthesizer.say("Hi Renjith.")
    except:
       print "exception occurred!"
       exc_type, exc_value, exc_traceback = sys.exc_info()
       traceback.print_exception(exc_type, exc_value, exc_traceback,
       limit=5, file=sys.stdout)
 
    print "done"
